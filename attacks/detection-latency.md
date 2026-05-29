# Detection latency — P1 MITRE ATT&CK simulations

| Attack | MITRE | Falco rule | Latency | Node |
|--------|-------|------------|---------|------|
| Cryptominer | T1496 | Drop and execute new binary in container | Xs | k8s-worker1 |
| Privileged escape | T1611 | Launch Privileged Container | Xs | k8s-worker1 |
| SA token abuse | T1528 | K8s Serviceaccount token file read | Xs | k8s-worker1 |
| kubectl exec | T1609 | Terminal shell in container | <1s | k8s-worker1 |

Fastest: Attack 4 — shell spawn triggers immediately
Slowest: Attack 1 — binary copy + exec sequence
