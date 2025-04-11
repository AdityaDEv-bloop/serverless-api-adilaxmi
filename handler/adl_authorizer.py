import json



def adlAuthorizer(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully Auth New!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
