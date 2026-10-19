# Security Hub CloudTrail Control Remediation

## Overview

AWS Security Hub CSPM was enabled to evaluate the security posture of the lab environment.

During the assessment, Security Hub identified a high-severity failed control related to AWS CloudTrail.

The objective of this exercise was to investigate the failed control, understand the security requirement, implement the remediation, and verify the resulting CloudTrail configuration.

---

## Detected Security Finding

### Control

`CloudTrail.1`

### Severity

`High`

### Compliance Status

`FAIL`

### Finding

Security Hub reported that CloudTrail should be enabled and configured with at least one multi-Region trail that includes both read and write management events.

---

## Why the Control Failed

CloudTrail Event History was already available and had been used to investigate AWS management activity such as the `RunInstances` API call.

However, CloudTrail Event History and a persistent CloudTrail trail are different capabilities.

### Event History

CloudTrail Event History provides recent management-plane activity that can be reviewed directly in the AWS console.

Example:

```text
AWS Console
    ↓
EC2 API
    ↓
RunInstances
    ↓
CloudTrail Event History
