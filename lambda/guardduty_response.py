import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    logger.info("GuardDuty event received")
    logger.info(json.dumps(event))

    detail = event.get("detail", {})

    severity = detail.get("severity")
    finding_type = detail.get("type", "Unknown")

    resource = detail.get("resource", {})
    instance_details = resource.get("instanceDetails", {})
    instance_id = instance_details.get("instanceId", "NotAvailable")

    logger.info("Finding type: %s", finding_type)
    logger.info("Severity: %s", severity)
    logger.info("Instance ID: %s", instance_id)

    response = {
        "mode": "DRY_RUN",
        "findingType": finding_type,
        "severity": severity,
        "instanceId": instance_id,
        "recommendedAction": "QUARANTINE_INSTANCE"
    }

    logger.info("Response decision: %s", json.dumps(response))

    return response
