# HCT-A2A Extension Specification v1

**Status**: Draft  
**Extension Name**: `hct-coordination`  
**Extension URI**: `https://github.com/stefanwiest/hct-a2a`  
**Version**: 1.0.0

---

## Abstract

This specification defines the `hct-coordination` extension for the A2A Protocol, adding coordination semantics derived from Harmonic Coordination Theory (HCT).

## Extension Registration

```json
{
  "extensions": {
    "hct-coordination": "1.0.0"
  }
}
```

## Capability Declaration

Agents supporting this extension declare it in their Agent Card:

```json
{
  "name": "My Agent",
  "extensions": ["hct-coordination"]
}
```

---

## Signals

### Core Signals (Shared with MCP)

| Signal | Method | Semantics |
|--------|--------|-----------|
| `cue` | `tasks/send` | Trigger agent activation |
| `fermata` | `tasks/sendSubscribe` | Hold for approval |
| `attacca` | `tasks/send` | Immediate transition |
| `vamp` | `tasks/sendSubscribe` | Repeat until condition |
| `caesura` | `tasks/cancel` | Full stop |

### A2A-Only Signals

| Signal | Method | Semantics |
|--------|--------|-----------|
| `tacet` | — | Agent inactive for section |
| `downbeat` | `notifications/message` | Global synchronization point |

---

## Message Format

HCT metadata is embedded in the `parts[].metadata` field:

```json
{
  "jsonrpc": "2.0",
  "method": "tasks/send",
  "params": {
    "id": "task-123",
    "message": {
      "role": "user",
      "parts": [{
        "type": "text",
        "text": "Analyze Q4 data",
        "metadata": {
          "hct": {
            "signal": "cue",
            "from": "orchestrator",
            "performance": {
              "tempo": "allegro",
              "dynamics": "f",
              "urgency": 8
            }
          }
        }
      }]
    }
  }
}
```

---

## Performance Parameters

### Tempo (Urgency)

| Value | Priority | Expected Latency |
|-------|----------|------------------|
| `largo` | batch | ~60s |
| `andante` | low | ~30s |
| `moderato` | normal | ~15s |
| `allegro` | high | ~5s |
| `presto` | realtime | ~1s |

### Dynamics (Resource Intensity)

| Value | Meaning | Budget Multiplier |
|-------|---------|-------------------|
| `pp` | Minimal (cache only) | 0.25x |
| `p` | Light (fast model) | 0.5x |
| `mf` | Standard | 1.0x |
| `f` | Heavy (reasoning model) | 1.5x |
| `ff` | Maximum (ensemble CoT) | 2.0x |

---

## Conditions

For `fermata` and `vamp` signals:

```json
{
  "hct": {
    "signal": "fermata",
    "conditions": {
      "hold_type": "human",
      "timeout_ms": 3600000
    }
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `hold_type` | enum | `human`, `governance`, `resource`, `quality` |
| `quality_threshold` | number | 0.0-1.0 for vamp release |
| `repeat_until` | string | Natural language condition |

---

## Context (Optional)

For debugging and observability:

```json
{
  "hct": {
    "signal": "cue",
    "context": {
      "movement": "financial_analysis",
      "objectives": ["identify_root_cause"]
    }
  }
}
```

---

## Compatibility

- **Backward Compatible**: Agents not supporting this extension ignore `hct` metadata.
- **MCP Alignment**: Core signals align with [hct-mcp-signals](https://github.com/stefanwiest/hct-mcp-signals).

---

## References

- [Canonical Spec](https://github.com/stefanwiest/genesis/tree/main/hct-spec/spec.yaml)
- [HCT Paper](https://stefanwiest.de/research/papers/harmonic-coordination-theory/)
- [A2A Protocol](https://github.com/a2aproject/a2a)
