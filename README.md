# HCT A2A Extension

**Harmonic Coordination Theory extension for Google A2A Protocol**

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

---

## Overview

This extension adds coordination semantics from [Harmonic Coordination Theory](https://stefanwiest.de/research/papers/harmonic-coordination-theory/) to the [Agent-to-Agent (A2A) Protocol](https://github.com/a2aproject/a2a). It allows agents to coordinate using musical signals like `cue`, `fermata` (hold), and `vamp` (loop), and control resource intensity via `dynamics`.

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

## Specification

The canonical signal definition is provided in **Protocol Buffers** format, auto-generated from the central [`hct-spec`](https://github.com/stefanwiest/hct-spec).

- [**spec/v1/hct.proto**](spec/v1/hct.proto) - Protobuf Definition
- [**spec/v1/spec.md**](spec/v1/spec.md) - Human Printable Spec and Schema

## Polyglot Samples

We provide reference implementations demonstrating the **Conductor/Performer** relationship in four languages:

| Language | Path | Concepts |
|---|---|---|
| **Python** | [`samples/python`](samples/python) | Full Conductor/Musician, `tempo`, `dynamics` |
| **TypeScript** | [`samples/ts`](samples/ts) | Node.js asynchronous actors, `vamp`, `attacca` |
| **Rust** | [`samples/rust`](samples/rust) | High-performance Tokio tasks, type-safe signals |
| **Go** | [`samples/go`](samples/go) | Struct-based Orchestration, `fermata`, `caesura` |

## Signals Reference

| Signal | Description | A2A Method |
|--------|-------------|------------|
| `cue` | Trigger agent activation | `tasks/send` |
| `fermata` | Hold for approval | `tasks/sendSubscribe` |
| `attacca` | Immediate transition | `tasks/send` |
| `vamp` | Repeat until condition | `tasks/sendSubscribe` |
| `caesura` | Full stop | `tasks/cancel` |
| `tacet` | Agent inactive (A2A only) | — |
| `downbeat` | Global sync point (A2A only) | `notifications/message` |

## Canonical Source

Signal definitions are derived from:
- **Source of Truth**: [`hct-spec/spec.yaml`](https://github.com/stefanwiest/hct-spec/blob/main/spec.yaml)

## Related

- [hct-mcp-signals](https://github.com/stefanwiest/hct-mcp-signals) - MCP extension (Python, npm, Rust, Go)
- [A2A Protocol](https://github.com/a2aproject/a2a)

## License

[Apache License 2.0](LICENSE)
