# Planned laptop-local advisory AI — Cloudflare Clef-Flash Q8_0

Sources: [current Hebrew proposal](https://docs.google.com/document/d/1fzNJpmtbakEgXjv7uT-z_8NCtRAehNbJFDoFE5lqjn0/edit) and [build checklist](https://docs.google.com/document/d/1hNu4UcTtAlyoXaPMbntPuTFcWa2hmmdRNgN7wtSWM7A/edit), updated 12 October 2026.

## Deployment and behavior

The intended Cloudflare Clef-Flash Q8_0 decision model will run in an isolated process on the **same laptop** that hosts navigation, mapping, event capture and the web server. There is no Raspberry Pi and no separate home-PC inference service. Model calls must never hold up motor control, command expiry or local stopping.

The [model documentation](https://huggingface.co/Cloudflare/clef-flash) describes multimodal image/video decisions expressed as scores for predefined choices, not arbitrary generated explanations. [GGUF distribution documentation](https://huggingface.co/bartowski/Cloudflare_clef-flash-GGUF) identifies a Q8_0 model and a separate multimodal projector. A suitable runtime and its API still need to be installed, verified and benchmarked on the selected laptop. Compatibility and performance are not demonstrated by the model-card description.

## Planned use

The ESP CAM S3 sends selected images to the laptop by WiFi. The laptop records an event ID, image, capture timestamp, approximate robot observation pose and trigger reason before asynchronously requesting model assessment. Initial questions concern visible blockage, obstacles, narrow openings and image adequacy.

Return model/runtime versions, scores and latency. UI labels distinguish possible hazard, no hazard detected and unknown; pending, timeout, failed requests or inadequate images cannot be silently interpreted as safe. Scores are not verified human-safety probabilities or validated hazard-detection metrics.

Test with labelled arena images. Measure false alarms, missed findings and latency while navigation and browser services are also running. Choose confidence thresholds only from actual evaluation. No AI output may authorize or disable motion safety.

## Network boundary

AI communication is local to the laptop through bounded IPC/API. It is **not** the school-required internet data exchange. That requirement needs a separate independently verified network use case.

See the implementation checklist for open decisions, dependencies and acceptance tests.