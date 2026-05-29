# Attack 2 — Privileged Container Escape

**MITRE Technique:** T1611 — Escape to Host
**Tactic:** Privilege Escalation
**Falco Rules:** Launch Privileged Container, Terminal shell in container

## What This Simulates
Attacker deploys a privileged container with the host filesystem mounted.
Uses nsenter to escape from the container into the host PID namespace.

## P3 Note
In P3 Kyverno blocks privileged:true at admission. Pod never schedules.

## Evidence
See evidence/ folder for screenshots.
