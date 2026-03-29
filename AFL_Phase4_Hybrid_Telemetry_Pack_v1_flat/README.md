# AFL Phase 4 Hybrid Telemetry Pack v1

This pack upgrades AFL from runtime scaffolding into a hybrid telemetry architecture:

- **File-based telemetry first**
- **Socket transport later using the same event schema**

It adds:

- event schema validation
- file telemetry ingestion
- socket adapter stub
- match result builder
- reward engine
- anti-abuse checks
- telemetry runner scripts
- multiple scenario files
- contract docs

This is designed for the current AFL demo path:
- Unreal gameplay first
- no real robots yet
- no live arena yet
- no real money
- no production EOS dependency for core gameplay proof
