import boto3
import datetime

# Initialize boto3 clients
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')
cloudtrail = boto3.client('cloudtrail')

# Define constants
SSH_PORT = 22
FAILED_ATTEMPTS_THRESHOLD = 3
TIMEOUT_DURATION = 3600  # seconds

def lambda_handler(event, context):
    # Parse the event
    detail = event['detail']
    user_name = detail['userIdentity']['userName']
    event_name = detail['eventName']
    source_ip = detail['sourceIPAddress']
    
    # Check if the event is a failed SSH login attempt
    if event_name == 'ConsoleLogin' and detail['responseElements']['ConsoleLogin'] == 'Failure':
        # Increment the failed attempt count
        metric_data = cloudwatch.get_metric_data(
            MetricDataQueries=[
                {
                    'Id': 'failedAttempts',
                    'MetricStat': {
                        'Metric': {
                            'Namespace': 'CustomMetrics',
                            'MetricName': 'FailedSSHLoginAttempts',
                            'Dimensions': [
                                {
                                    'Name': 'UserName',
                                    'Value': user_name
                                },
                            ],
                        },
                        'Period': 300,
                        'Stat': 'Sum',
                    },
                    'ReturnData': True,
                },
            ],
            StartTime=datetime.datetime.utcnow() - datetime.timedelta(minutes=15),
            EndTime=datetime.datetime.utcnow()
        )
        
        failed_attempts = 0
        if metric_data['MetricDataResults'][0]['Values']:
            failed_attempts = int(metric_data['MetricDataResults'][0]['Values'][0])
        
        failed_attempts += 1
        
        # Put the updated metric
        cloudwatch.put_metric_data(
            Namespace='CustomMetrics',
            MetricData=[
                {
                    'MetricName': 'FailedSSHLoginAttempts',
                    'Dimensions': [
                        {
                            'Name': 'UserName',
                            'Value': user_name
                        },
                    ],
                    'Value': failed_attempts,
                    'Unit': 'Count'
                },
            ]
        )
        
        # If failed attempts exceed threshold, block the user
        if failed_attempts >= FAILED_ATTEMPTS_THRESHOLD:
            block_user(user_name, source_ip)
            
            # Reset the failed attempts count
            cloudwatch.put_metric_data(
                Namespace='CustomMetrics',
                MetricData=[
                    {
                        'MetricName': 'FailedSSHLoginAttempts',
                        'Dimensions': [
                            {
                                'Name': 'UserName',
                                'Value': user_name
                            },
                        ],
                        'Value': 0,
                        'Unit': 'Count'
                    },
                ]
            )

def block_user(user_name, source_ip):
    # Block the user by modifying security group or disabling the user
    security_groups = ec2.describe_security_groups(
        Filters=[
            {
                'Name': 'ip-permission.from-port',
                'Values': [str(SSH_PORT)]
            },
            {
                'Name': 'ip-permission.to-port',
                'Values': [str(SSH_PORT)]
            },
            {
                'Name': 'ip-permission.cidr',
                'Values': [f'{source_ip}/32']
            }
        ]
    )['SecurityGroups']
    
    for sg in security_groups:
        ec2.revoke_security_group_ingress(
            GroupId=sg['GroupId'],
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': SSH_PORT,
                    'ToPort': SSH_PORT,
                    'IpRanges': [
                        {
                            'CidrIp': f'{source_ip}/32'
                        },
                    ]
                },
            ]
        )
    
    print(f"Blocked IP {source_ip} for user {user_name}")
