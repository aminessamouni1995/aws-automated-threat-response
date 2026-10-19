# CloudTrail RunInstances Investigation

## Overview

AWS CloudTrail was used to investigate the management-plane activity generated when the lab EC2 workload was launched.

The objective was to understand how an action performed through the AWS Management Console is represented as an AWS API event and how CloudTrail can be used during security investigations.

---

## Investigated Event

### Event Name

`RunInstances`

### Event Source

`ec2.amazonaws.com`

### Region

`us-east-1`

### Read Only

`false`

The `RunInstances` API operation modifies AWS infrastructure by creating one or more EC2 instances.

---

## Investigation Questions

The CloudTrail event was reviewed to answer:

- Who launched the instance?
- What API operation was executed?
- When did the activity occur?
- From which source IP did the request originate?
- Which AWS service received the request?
- Which AWS Region was used?
- Which EC2 instance was created?
- Which Security Group was attached?
- Was a public IP assigned?
- Which EC2 configuration parameters were requested?

---

## Important CloudTrail Fields

### `userIdentity`

Identifies the IAM principal that performed the AWS API operation.

This can include:

- IAM user
- Assumed role
- Federated identity
- AWS service
- Temporary session

---

### `eventTime`

Represents when the API operation occurred.

This is important when building an incident timeline.

---

### `eventSource`

For this event:

`ec2.amazonaws.com`

This identifies Amazon EC2 as the AWS service receiving the API request.

---

### `eventName`

For this investigation:

`RunInstances`

This identifies the API operation that launched the EC2 workload.

---

### `awsRegion`

The workload was launched in:

`us-east-1`

---

### `sourceIPAddress`

CloudTrail records the source associated with the API request.

In a real investigation this field can help identify:

- Expected administrator access
- Suspicious external access
- VPN or corporate egress
- Compromised credentials

Sensitive source IP information has been removed from the public project.

---

### `userAgent`

The user agent provides context about how the API request was generated.

Examples can include:

- AWS Management Console
- AWS CLI
- AWS SDK
- Automated services or scripts

This can help distinguish manual administrator activity from automation.

---

## Request Parameters

The `requestParameters` section represents what the caller requested AWS to create.

Relevant values included:

- EC2 instance type
- AMI
- Security Group
- Network interface settings
- Public IP configuration
- Metadata service configuration
- Instance tags

The lab instance was launched with:

- Instance type: `t2.micro`
- No public IPv4 address
- Normal workload Security Group
- IMDSv2 required

---

## Response Elements

The `responseElements` section represents what AWS actually created or returned after processing the API request.

Relevant information included:

- EC2 instance ID
- Private IP address
- Availability Zone
- VPC
- Subnet
- Network interface
- Security Group
- Instance state

This allows an investigator to correlate the API request with the resource that was actually created.

---

## Request vs Response

A key investigation concept demonstrated in this lab was:

```text
requestParameters
        ↓
What the caller requested

responseElements
        ↓
What AWS actually created or returned
