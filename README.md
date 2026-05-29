# k8s-soc-foundation

**Project 1 - DevSecOps PortfolioI**

Hardened Kubernetes cluster on Hetzner Cloud running 4 real MITRE ATT&CK
simulations with Falco detection, AI-generated alert explanations,
and full observability via Loki + Grafana.

## Stack

| Component | Purpose |
|-----------|---------|
| kubeadm 1.28 | Cluster bootstrapping |
| Calico | CNI + NetworkPolicy |
| Falco | Runtime threat detection |
| Loki + Promtail | Log aggregation |
| Grafana | Dashboards |
| Trivy Operator | CVE scanning |
| GPT-4o-mini | AI alert explanations → Slack |

## MITRE ATT&CK Coverage

| Attack | Technique | Falco Rule | Detection Latency | Evidence |
|--------|-----------|------------|-------------------|---------|
| Cryptominer | T1496 Resource Hijacking | Drop and execute new binary | Xms | [📸](attacks/01-cryptominer/evidence/) |
| Privileged escape | T1611 Escape to Host | Launch Privileged Container | Xms | [📸](attacks/02-privileged-escape/evidence/) |
| SA token abuse | T1528 Steal App Access Token | K8s SA token file read | Xms | [📸](attacks/03-sa-token-abuse/evidence/) |
| kubectl exec | T1609 Container Admin Command | Terminal shell in container | Xms | [📸](attacks/04-kubectl-exec/evidence/) |

## Hardening

CIS Kubernetes Benchmark via kube-bench:
- Before: 11 FAIL → After: 7 FAIL (4 failures resolved)
- See [hardening/](hardening/) for full JSON reports

## AI Layer

Every Falco alert above Warning priority triggers the AI explainer:
Falcosidekick → GPT-4o-mini → plain English explanation + immediate
action → Slack within seconds of detection.

## Architecture Narrative

This is Project 1 of an Attack → Detect → Prevent → Respond
portfolio. OPA Gatekeeper, Kyverno, and Calico NetworkPolicies are
intentionally absent — those are added in Project 2, where all four
attacks are re-run against a hardened cluster to prove what gets blocked.

## Build Log

- [Session 1 & 2 — Infrastructure Struggles: conntrack, audit logs, Falco eBPF on Hetzner](link-coming-soon)
- [Attack 1 — Cryptominer Detection with Falco (T1496)](link-coming-soon)
- [Attack 2 — Privileged Container Escape (T1611)](link-coming-soon)
- [Attack 3 — Service Account Token Abuse (T1528)](link-coming-soon)
- [Attack 4 — kubectl exec Detection (T1609)](link-coming-soon)

## Certs
Sophos Firewall Architect · CCNA
CKA (coming soon)

# k8s-soc-foundation
