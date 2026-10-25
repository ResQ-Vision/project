#include "../shared/protocol.h"
#include <assert.h>
#include <stdio.h>
using namespace led_demo;
int main() {
  auto m = parse("LED FFFFFFFF 1");
  assert(m.kind == Kind::led && m.id == 0xffffffff && m.on);
  assert(parse("GET 00000001").kind == Kind::get);
  assert(parse("ACK 1234ABCD 0").kind == Kind::ack);
  auto ack = parse("ACK 1234ABCD 0");
  assert(matches(ack, 0x1234abcd, false, true));
  assert(matches(ack, 0x1234abcd, true, false));
  assert(!matches(ack, 0x1234abce, true, false)); // Stale/wrong ID.
  assert(!matches(ack, 0x1234abcd, true, true));  // Wrong resulting state.
  assert(!matches(parse("LED 1234ABCD 0"), 0x1234abcd, true, false));
  const char *bad[] = {"", "LED 00000001 2", "LED 00000001 1 junk", "GET 0000000G",
                       "GET 100000001", "LED -0000001 1", "ACK 00000001", "GET 0000abcd"};
  for (auto s : bad) assert(parse(s).kind == Kind::invalid);
  LineReader r;
  for (char c : "LED 00000001 1") if (c) assert(!r.push(c));
  assert(r.push('\n') && parse(r.data).kind == Kind::led);
  for (int i = 0; i < 64; ++i) assert(!r.push('X'));
  for (char c : "LED 00000001 1") if (c) assert(!r.push(c));
  assert(!r.push('\n')); // Embedded valid suffix cannot become a command.
  for (char c : "GET 00000002") if (c) r.push(c);
  assert(r.push('\n') && parse(r.data).id == 2);
  r.push('L'); r.invalidate();
  assert(!r.push('\n'));
  r.push('G'); r.push('\0'); assert(!r.push('\n'));
  puts("Protocol tests passed: bounds, invalid input, recovery and IDs");
}
