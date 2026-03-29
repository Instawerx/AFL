# AFL Phase 7 — Network Layer + Live Player Connections

## Purpose

Introduce a live local network session server so AFL can move from simulated multiplayer into connected client sessions.

## Included pieces

- TCP session server
- client simulator
- state sync scaffolding
- session state artifact output

## Outputs

- network_session_state.json

## Why this matters

This is the first AFL layer where connected clients can join, ready up, and push the session into a live started state over a real local transport.
