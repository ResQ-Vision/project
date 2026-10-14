# Firmware instructions

Read root rules, module README, safety document and applicable contracts.
Pin board/toolchain and record pin, timing and power assumptions before hardware code.
Never let networking, camera/sensor work or blocking bus calls defeat local stop freshness.
Motion ESP32 is the final authority across direct C3 and laptop links. Use front-steering
geometry; distance sensing uses the 2D LiDAR, with no separate ToF. No cliff-detection claim.
Fixtures/native tests are software evidence only. Log equipment and actual measured results.
