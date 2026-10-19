# AWS Automated Threat Detection & Response

## Project Status

🚧 In Progress

This project demonstrates a hands-on AWS Cloud Security Engineering workflow for threat detection, security posture management, audit logging, event-driven automation, and incident response.

The environment is built as a controlled AWS security lab using Amazon EC2, AWS CloudTrail, Amazon GuardDuty, AWS Security Hub CSPM, Amazon EventBridge, AWS Lambda, IAM, Amazon CloudWatch, and Amazon S3.

---

## Project Architecture

```text
EC2 Workload
    │
    ├── CloudTrail
    │      └── Audit logging
    │
    └── GuardDuty
           │
           └── Threat detection
                  │
                  ▼
             EventBridge
                  │
          Security filtering
                  │
                  ▼
               Lambda
                  │
          Response automation
                  │
                  ▼
          Quarantine Security Group

Supporting services:

Security Hub CSPM
→ Security posture and compliance

CloudWatch
→ Automation logging and validation

S3
→ Persistent CloudTrail log storage

IAM
→ Least-privilege permissions
