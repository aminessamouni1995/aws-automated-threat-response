# GuardDuty C2 Finding Analysis

## Finding Summary

During the AWS security lab, Amazon GuardDuty sample findings were generated to validate the threat detection and automated response workflow.

The selected finding represented Command & Control activity detected from an EC2 workload.

### Finding Type

`Backdoor:Runtime/C&CActivity.B!DNS`

### Severity

`High`

### Action Type

`DNS_REQUEST`

### Protocol

`UDP`

### Blocked

`false`

---

## Security Interpretation

The finding indicates that a workload performed a DNS query for a domain associated with known Command & Control infrastructure.

Command & Control communication can be used by an attacker to communicate with a compromised system after initial access.

A typical attack flow could be:

```text
Compromised workload
        ↓
Malicious process
        ↓
DNS query
        ↓
Command & Control domain
        ↓
Attacker infrastructure
