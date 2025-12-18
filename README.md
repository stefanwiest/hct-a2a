# HCT A2A Extension

**Harmonic Coordination Theory extension for Google A2A Protocol**

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

---

## Overview

This extension adds coordination semantics from [Harmonic Coordination Theory](https://stefanwiest.de/research/papers/harmonic-coordination-theory/) to the [Agent-to-Agent (A2A) Protocol](https://github.com/a2aproject/a2a).

## Extension Registration

```json
{
  "extensions": [
    {
      "uri": "https://github.com/stefanwiest/hct-a2a",
      "description": "HCT coordination signals for multi-agent orchestration"
    }
  ]
}
```

## Signals

| Signal | Description | A2A Method |
|--------|-------------|------------|
| `cue` | Trigger agent activation | `tasks/send` |
| `fermata` | Hold for approval | `tasks/sendSubscribe` |
| `attacca` | Immediate transition | `tasks/send` |
| `vamp` | Repeat until condition | `tasks/sendSubscribe` |
| `caesura` | Full stop | `tasks/cancel` |
| `tacet` | Agent inactive (A2A only) | — |
| `downbeat` | Global sync point (A2A only) | `notifications/message` |

## Specification

See [spec/v1/spec.md](spec/v1/spec.md) for the formal specification.

## Schema

See [spec/v1/schema.json](spec/v1/schema.json) for JSON Schema validation.

## Canonical Source

Signal definitions are derived from:
- **Source of Truth**: [`hct-spec/spec.yaml`](https://github.com/stefanwiest/genesis/tree/main/hct-spec/spec.yaml)

## Related

- [hct-mcp-signals](https://github.com/stefanwiest/hct-mcp-signals) - MCP extension (Python, npm, Rust, Go)
- [A2A Protocol](https://github.com/a2aproject/a2a)

## License

[Apache License 2.0](LICENSE)
