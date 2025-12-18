# HCT A2A Python Sample

This sample demonstrates an HCT-compliant **Performer** (Server) and **Conductor** (Client).

## Setup

```bash
pip install -r requirements.txt
```

## Running

1. **Start the Performer (Musician)**:
   ```bash
   python -m server.main
   ```
   The server listens on `http://localhost:8000`.

2. **Run the Conductor**:
   ```bash
   python -m client.main
   ```

## HCT Concepts Demonstrated

- **Tempo**: The Performer adjusts its processing delay based on `largo` (slow) vs `allegro` (fast).
- **Dynamics**: The Performer provides more verbose output for `ff` (fortissimo) requests.
