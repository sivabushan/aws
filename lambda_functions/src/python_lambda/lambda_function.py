import os

def handler(event, context):
    # return {
    #     'statusCode': 200,
    #     'message': "Hello from python lambda function!"
    # }
    env = os.getenv("ENV_VAR_TEST")
    return {
        'statusCode': 200,
        'message': env
    }