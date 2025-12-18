# HCT A2A Extension

**Harmonic Coordination Theory extension for Google A2A Protocol**

> Status: **Draft** - Work in Progress

## Overview

This extension adds coordination semantics from [Harmonic Coordination Theory](https://stefanwiest.de/research/papers/harmonic-coordination-theory/) to the [Agent-to-Agent (A2A) Protocol](https://github.com/a2aproject/a2a).

## Specification

See [spec/v1/spec.md](spec/v1/spec.md) for the formal specification.

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

## Canonical Specification

Signal definitions are derived from:
- **Source of Truth**: [`hct-spec/spec.yaml`](https://github.com/stefanwiest/genesis/tree/main/hct-spec/spec.yaml)

## Related

- [hct-mcp-signals](https://github.com/stefanwiest/hct-mcp-signals) - MCP extension
- [A2A Extensions Overview](https://developers.googleblog.com/en/a2a-extensions-empowering-custom-agent-functionality/)
- [Twilio A2A Latency Extension](https://github.com/twilio-labs/a2a-latency-extension) - Reference implementation

## License

Apache 2.0
