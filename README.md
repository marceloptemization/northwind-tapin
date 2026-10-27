# Northwind Health: TapIn & Relay

> Demo repository. Northwind Health is a fictional company; nothing here is real or production code.

TapIn is badge-tap sign-on for shared clinical workstations. Relay handles hand-off of shared mobile devices between shifts.

Product context (PRDs, decisions, runbooks) lives in the Northwind Engineering Hub in Notion. Work is tracked in the GitHub Project "Northwind Delivery".

## Layout

- `src/tapin/`: workstation agent and session broker
- `src/relay/`: device pool service
- `docs/`: architecture notes kept next to the code

## Working agreement

- Every PR references its PRD (Notion link) in the description.
- No PHI anywhere: issues, PRs, commits, fixtures. Use synthetic records.
