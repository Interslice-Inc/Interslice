import json
import boto3
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    sns_client = boto3.client('sns')
    topic_arn = 'arn:aws:sns:us-east-1:905418121907:SSHLambdaAlerts'
    
    try:
        message = json.dumps(event)
        subject = 'SSH Login Attempt Alert'
        
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject=subject
        )
        
        logger.info(f'SNS publish response: {response}')
        
        return {
            'statusCode': 200,
            'body': json.dumps('Alert sent!')
        }
    except Exception as e:
        logger.error(f'Error publishing SNS message: {e}')
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to send alert.')
        }

