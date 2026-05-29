# Hardening Steps Applied

1. Disabled anonymous auth on API server
2. Enabled audit logging with custom policy
3. Disabled default service account token automount
4. Applied pod-security baseline enforcement on default namespace
5. Verified NodeRestriction admission plugin active

## kube-apiserver flags added
- --anonymous-auth=false
- --audit-log-path=/var/log/kubernetes/audit.log
- --audit-log-maxage=30
- --audit-log-maxbackup=10
- --audit-log-maxsize=100
- --audit-policy-file=/etc/kubernetes/audit-policy.yaml
