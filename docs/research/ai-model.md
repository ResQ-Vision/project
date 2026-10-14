# AI model verification plan

Intended model: Cloudflare Clef-Flash Q8_0 on the same laptop as PC Server.
Model identity, weight/projector pairing, runtime compatibility and concurrent-load
performance are unresolved. Historical references include:
- https://huggingface.co/Cloudflare/clef-flash
- https://huggingface.co/bartowski/Cloudflare_clef-flash-GGUF
- https://huggingface.co/ggml-org/Clef-Flash-GGUF

These links are research leads from previous documents; this migration did not fetch
weights or benchmark them. Do not pin an API from an old assistant suggestion.
The proposal's ~9B / ~9.68 GB and `/v1/systemone` claims remain unverified.

Before integration record official model ID/license, weight and projector checksums,
runtime/version and actual image-capable request/response example. Validate the adapter
against [proposed inference schemas](../../contracts/ai/README.md), keeping raw output internal.

Use fixed image/category questions and labeled arena images. Evaluate missed findings,
false alarms, poor-image behavior, response shape, score meaning and latency. Scores are
not calibrated human-safety probabilities. Select thresholds from measurements.

Measure laptop CPU/GPU/RAM and server/control responsiveness under simultaneous workloads.
Bound image size, queue, memory, retries and timeout. Failure is unknown/unavailable.
No model response can arm motors, issue movement, clear stops or override freshness.
