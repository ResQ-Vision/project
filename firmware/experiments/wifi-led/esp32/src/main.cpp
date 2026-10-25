#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <esp_system.h>
#include "../../shared/protocol.h"
#include "web_page.h"

// Classic ESP32-WROOM development board only; verify the module marking.
constexpr int RX_PIN = 16;
constexpr int TX_PIN = 17;
constexpr char SSID[] = "ResQ-LED-Lab";
constexpr char PASSWORD[] = "resq-led-lab"; // Demo password; change before sharing.
HardwareSerial bridge(2);
WebServer server(80);
uint32_t sequence;

bool transact(bool set, bool requested, bool &reported) {
  while (bridge.available()) bridge.read();
  uint32_t id = ++sequence;
  char command[20];
  if (set) snprintf(command, sizeof(command), "LED %08lX %d\n", static_cast<unsigned long>(id), requested);
  else snprintf(command, sizeof(command), "GET %08lX\n", static_cast<unsigned long>(id));
  bridge.print(command);
  led_demo::LineReader reader;
  uint32_t start = millis();
  while (millis() - start < 750) {
    while (bridge.available()) {
      if (!reader.push(static_cast<char>(bridge.read()))) continue;
      auto m = led_demo::parse(reader.data);
      if (m.kind == led_demo::Kind::ack && m.id == id) {
        reported = m.on;
        return led_demo::matches(m, id, set, requested);
      }
    }
    delay(1);
  }
  return false;
}

void respond(bool set = false, bool requested = false) {
  bool on = false;
  server.sendHeader("Cache-Control", "no-store");
  if (!transact(set, requested, on)) {
    server.send(504, "application/json", "{\"error\":\"STM32 did not confirm. Check power, firmware, TX/RX and GND. LED state is unknown.\"}");
    return;
  }
  server.send(200, "application/json", on ? "{\"on\":true}" : "{\"on\":false}");
}

void setup() {
  Serial.begin(115200);
  bridge.begin(115200, SERIAL_8N1, RX_PIN, TX_PIN);
  sequence = esp_random();
  WiFi.mode(WIFI_AP);
  if (!WiFi.softAP(SSID, PASSWORD, 1, false, 1)) {
    Serial.println("Wi-Fi AP startup failed; reset ESP32 to retry.");
    while (true) delay(1000);
  }
  server.on("/", HTTP_GET, []() {
    server.sendHeader("Cache-Control", "no-store");
    server.send_P(200, "text/html", WEB_PAGE);
  });
  server.on("/api/status", HTTP_GET, []() { respond(); });
  const char *headers[] = {"Content-Type"};
  server.collectHeaders(headers, 1);
  server.on("/api/led", HTTP_POST, []() {
    // JSON-only, with no CORS support: ordinary cross-origin forms cannot change it.
    if (server.header("Content-Type") != "application/json") {
      server.send(415, "application/json", "{\"error\":\"Use application/json\"}"); return;
    }
    String body = server.arg("plain");
    if (body != "{\"on\":true}" && body != "{\"on\":false}") {
      server.send(400, "application/json", "{\"error\":\"Expected a single boolean on field\"}"); return;
    }
    respond(true, body == "{\"on\":true}");
  });
  server.onNotFound([]() { server.send(404, "text/plain", "Not found"); });
  server.begin();
  Serial.print("Join Wi-Fi: "); Serial.println(SSID);
  Serial.print("Open http://"); Serial.println(WiFi.softAPIP());
}
void loop() { server.handleClient(); }
