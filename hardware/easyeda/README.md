# Superseded ESP32 electrical reference

This directory preserves the 19 October 2026 ESP32 candidate chart, generator and previews.
The owner selected Hiwonder V1.2 STM32 on 21 October; these files are not a current wiring
plan. Do not reuse their ESP32 GPIO assignments, driver/IMU/servo parts or power budget.
The generator only regenerates this historical design. Existing tests check its historical
structure, not STM32 compatibility. See [current hardware](../../docs/hardware/stm32-controller.md)
and [supersession details](../../docs/hardware/electrical-chart.md). A new reviewed V1.2
schematic and pin matrix are required before wiring integration.
