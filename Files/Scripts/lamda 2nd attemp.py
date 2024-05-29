import boto3

def lambda_handler(event, context):
    client = boto3.client('lambda')
    
    if event['type'] == 'SSH':
        if 'attempts' in event:
            event['attempts'] += 1
        else:
            event['attempts'] = 1
        
        if event['attempts'] >= 3:
            # Timeout user logic here
            client.invoke(FunctionName='timeout_user_function', Payload='{"user": "username"}')
    
    return {
        'statusCode': 200,
        'body': 'SSH attempt processed successfully'
    }

