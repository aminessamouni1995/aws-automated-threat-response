# CloudWatch Automation Validation

## Overview

Amazon CloudWatch Logs was used to validate the event-driven security automation pipeline built in this project.

The objective was to confirm that a qualifying GuardDuty finding successfully passed through Amazon EventBridge and invoked the AWS Lambda response function.

The Lambda function was intentionally operating in `DRY_RUN` mode during this validation phase.

---

## Validated Architecture

```text
Amazon GuardDuty
        ↓
High-Severity C2 Finding
        ↓
Amazon EventBridge
        ↓
Security Event Pattern
        ↓
AWS Lambda
        ↓
CloudWatch Logs
