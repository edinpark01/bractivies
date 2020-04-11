import json


def respond(body, code):
    """ Wrapper around HTTP response """
    return {'statusCode': code, 'body': json.dumps(body, indent=4)}