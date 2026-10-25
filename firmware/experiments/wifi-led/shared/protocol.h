#pragma once
#include <stdint.h>
#include <stddef.h>
#include <string.h>

namespace led_demo {
enum class Kind { invalid, get, led, ack };
struct Message { Kind kind = Kind::invalid; uint32_t id = 0; bool on = false; };

// Fixed-width IDs avoid ambiguous parsing and integer overflow.
inline Message parse(const char *line) {
  Message m;
  size_t n = strlen(line);
  if (n != 12 && n != 14) return m;
  if (n == 12 && memcmp(line, "GET ", 4) == 0) m.kind = Kind::get;
  if (n == 14 && line[12] == ' ' && (line[13] == '0' || line[13] == '1')) {
    if (memcmp(line, "LED ", 4) == 0) m.kind = Kind::led;
    if (memcmp(line, "ACK ", 4) == 0) m.kind = Kind::ack;
    m.on = line[13] == '1';
  }
  if (m.kind == Kind::invalid) return m;
  for (size_t i = 4; i < 12; ++i) {
    char c = line[i];
    if (!((c >= '0' && c <= '9') || (c >= 'A' && c <= 'F'))) return Message{};
    m.id = (m.id << 4) | static_cast<uint32_t>(c <= '9' ? c - '0' : c - 'A' + 10);
  }
  return m;
}

inline bool matches(const Message &m, uint32_t id, bool set, bool requested) {
  return m.kind == Kind::ack && m.id == id && (!set || m.on == requested);
}

// Oversized/corrupted frames are discarded through newline, never parsed as a suffix.
struct LineReader {
  char data[32] = {};
  size_t used = 0;
  bool dropping = false;
  void invalidate() { used = 0; dropping = true; }
  bool push(char c) {
    if (c == '\n') {
      bool ready = !dropping && used > 0;
      data[used] = '\0';
      used = 0;
      dropping = false;
      return ready;
    }
    if (dropping) return false;
    if (c < 32 || c > 126 || used >= sizeof(data) - 1) { invalidate(); return false; }
    data[used++] = c;
    return false;
  }
};
}
