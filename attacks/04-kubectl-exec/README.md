# Attack 4 — kubectl exec into Running Container

**MITRE Technique:** T1609 — Container Administration Command
**Tactic:** Execution
**Falco Rule:** Terminal shell in container

## What This Simulates
Attacker with kubectl access execs into a legitimate running container.
This is the fastest detection — sub-second latency.

## P3 Note
In P3 OPA Gatekeeper audit flags exec attempts. Falco still detects.
The distinction: detect vs alert vs block.

## Evidence
See evidence/ folder for screenshots.
