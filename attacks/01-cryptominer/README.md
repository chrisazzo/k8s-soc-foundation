# Attack 1 — Cryptominer Deployment

**MITRE Technique:** T1496 — Resource Hijacking
**Tactic:** Impact
**Falco Rule:** Drop and execute new binary in container

## What This Simulates
Attacker deploys a container and copies a binary to /tmp at runtime,
then executes it — simulating a cryptominer drop. The binary name
(xmrig) and stratum protocol string are both detected by Falco.

## Detection
Falco fires Critical alert on:
- Binary copied to /tmp and executed
- Process name matches cryptominer list
- Command line contains stratum+tcp

## P3 Note
In P3 this same YAML is re-run against OPA Gatekeeper + Kyverno.
The pod is blocked at admission — never schedules. Compare evidence folders.
