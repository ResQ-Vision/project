> Historical review dated 6 October. Current live document and context README supersede unresolved-goal, camera and optional-sensor statements below.

# Proposal review after AI expansion

Reviewed the live Google Doc against the repository context, original proposal template, current-year school circular, and current model documentation. The editable Google Doc remains the authoritative proposal. User edits to component quantities were preserved.

The original AI mention was brief. A dedicated section now explains the model, local home-PC inference, predefined decisions rather than generated explanations, image-projector requirement, camera-event capture, selected-frame requests, map association, phone display, background processing, uncertainty/failure handling, and labelled-scene evaluation. The Hebrew section is also saved in `proposal-ai-section.md` for context.

Other gaps filled: WiFi data/command transport with timestamps and stale-command checks; a distinction between local phone access and a controller's actual internet exchange; filtering/invalid sensor readings; metric range measurement; and sourced TurtleBot3 teleoperation and planar SLAM examples. These examples are comparison references, not a commitment to buy TurtleBot3 or implement full SLAM.

Remaining team/supervisor decisions: exact goal and need, final title and cover details, two-controller/independent-subsystem compliance, hardware models and budget, protocol allocation, internet service, capture triggers/category definitions, test arena, numerical acceptance targets and full proposal deadline. Home-PC hardware suitability has already been checked by the user; project-specific integration and performance remain future implementation work.

At the initial audit, the original tldraw Page 1 showed Raspberry Pi and simulated cleaning rather than the then-current laptop architecture. This finding is resolved by the later Raspberry Pi update recorded below. Final school submission also requires one PDF, while Google Docs remains the editable working format.

All six native-exported pages were rasterized and visually reviewed after the changes. The abstract and need sections still fit on their existing page, and the expanded AI section occupies the sixth page. No prototype operation or AI accuracy is claimed as tested.

Sources:

- https://huggingface.co/Cloudflare/clef-flash
- https://huggingface.co/bartowski/Cloudflare_clef-flash-GGUF
- https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_operation/
- https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/
- Original proposal DOCX and תשפ״ז circular in `resources/originals/`.

## Resolution: current Raspberry Pi plan

The user requested fixing the audit findings and adding Raspberry Pi to the current plan. The Google Doc now assigns ESP local motor control/stopping, Pi onboard capture/mapping/navigation/backend, laptop operation/testing and home-PC AI. Page 1 in tldraw was updated, removing simulated cleaning, adding camera/AI, marking optional sensors and restoring handwriting labels. Its new export is inserted in the proposal. Diagram/component explanations, per-computer quantities, communication planning and final-PDF submission requirement were corrected.

The exact goal/problem and missing school/person fields remain intentionally open. Pi model, camera/sensor models, budget, numeric test targets, internet endpoint and supervisor approval of the full two-subsystem requirements remain unresolved; processor count alone is not acceptance.

After formatting repair, all six pages of the final native PDF export were visually checked. The abstract/need remain within their template page limits. The block diagram, explanation table, component list and AI section are readable. The document font stays Arial; the handwriting request applied to tldraw labels.
