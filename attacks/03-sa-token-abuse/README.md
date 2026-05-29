# Attack 3 — Service Account Token Abuse

**MITRE Technique:** T1528 — Steal Application Access Token
**Tactic:** Credential Access
**Falco Rules:** K8s Serviceaccount token file read, Contact K8S API Server From Container

## What This Simulates
Attacker reads the auto-mounted service account token and uses it
to authenticate to the Kubernetes API and enumerate cluster resources.

## P3 Note
In P3 the default SA has no permissions and automount is disabled.
Falco still detects the read — but the API calls return 403.

## Evidence
See evidence/ folder for screenshots.
