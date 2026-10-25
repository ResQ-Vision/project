#include <Arduino.h>
#include <Serial.h>
#include "../../shared/protocol.h"

// PROVISIONAL V1.2 board profile: verify PE10 active-low before flashing.
// Constructor order is RX, TX. Explicit ALT1 selects USART3/AF7;
// this generic variant otherwise maps plain PC10/PC11 to UART4/AF8.
Uart bridge(PC_11_ALT1, PC_10_ALT1);
led_demo::LineReader reader;
uint32_t lastByte = 0;

// Run entirely from the internal 16 MHz HSI; no crystal/PLL assumption.
extern "C" void SystemClock_Config(void) {
  RCC_OscInitTypeDef osc = {};
  osc.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  osc.HSIState = RCC_HSI_ON;
  osc.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  osc.PLL.PLLState = RCC_PLL_OFF;
  if (HAL_RCC_OscConfig(&osc) != HAL_OK) while (true) {}
  RCC_ClkInitTypeDef clk = {};
  clk.ClockType = RCC_CLOCKTYPE_SYSCLK | RCC_CLOCKTYPE_HCLK |
                  RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2;
  clk.SYSCLKSource = RCC_SYSCLKSOURCE_HSI;
  clk.AHBCLKDivider = RCC_SYSCLK_DIV1;
  clk.APB1CLKDivider = RCC_HCLK_DIV1;
  clk.APB2CLKDivider = RCC_HCLK_DIV1;
  if (HAL_RCC_ClockConfig(&clk, FLASH_LATENCY_0) != HAL_OK) while (true) {}
}

void setup() {
  __HAL_RCC_GPIOE_CLK_ENABLE();
  digitalWrite(PE10, HIGH);  // Preload OFF before enabling output.
  pinMode(PE10, OUTPUT);
  bridge.begin(115200, SERIAL_8N1);
}

void loop() {
  if (reader.used && millis() - lastByte > 100) reader.invalidate();
  while (bridge.available()) {
    char c = static_cast<char>(bridge.read());
    lastByte = millis();
    if (!reader.push(c)) continue;
    auto m = led_demo::parse(reader.data);
    if (m.kind != led_demo::Kind::get && m.kind != led_demo::Kind::led) continue;
    if (m.kind == led_demo::Kind::led) digitalWrite(PE10, m.on ? LOW : HIGH);
    // Reports GPIO readback, not optical confirmation that the LED illuminated.
    char ack[20];
    snprintf(ack, sizeof(ack), "ACK %08lX %d\n", static_cast<unsigned long>(m.id),
             digitalRead(PE10) == LOW ? 1 : 0);
    bridge.print(ack);
  }
}
