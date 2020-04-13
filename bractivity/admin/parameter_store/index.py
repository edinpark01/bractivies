import boto3
#TODO: Move the below inport to AWS Lambda Layer
from utils import respond

client = boto3.client('ssm')


def lambda_handler(event, context):
    """
    This function handles AWS System Manager's Parameter Store.
    :param event: Ought to include the following:
        :action: api-call argument specifiying what kind of action
                 is to be performed, options available are:
                    -> list, create, delete
    :param context: Meh
    """
    body = {k.lower(): v for k, v in event.items() if k.lower() == 'body'}

    if not body or not body.get('body'):
        return respond({'error', 'missing request body'}, 400)

    parameter_info = body.get('body')

    try:
        response = client.put_parameter(
            Name        = parameter_info['name'],
            Description = parameter_info['description'],
            Value       = parameter_info['value'],
            Type        = 'SecureString',
            Overwrite   = True,
            Tier        ='Standard',
        )
    except Exception as e:
        return respond(str(e), 500)

    return respond(response, 200)
