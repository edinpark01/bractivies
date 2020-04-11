import requests
import os

# TODO: Move the below import into AWS Lambda Layer
from utils import respond

CLIENT_ID     = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TOKEN_REFRESH = os.getenv('TOKEN_REFRESH')


def lambda_handler(event, context):
    post_data = dict(
        client_id     = CLIENT_ID,        # The application’s ID, obtained during registration.

        client_secret = CLIENT_SECRET,    # The application’s secret, obtained during registration.

        grant_type    = 'refresh_token',  # The grant type for the request. When refreshing an access
                                          # token, must always be "refresh_token".

        refresh_token = TOKEN_REFRESH)    # The refresh token for this user, to be used to get the
                                          # next access token for this user. Please expect
                                          # that this value can change anytime you retrieve
                                          # a new access token. Once a new refresh token
                                          # code has been returned, the older code will no longer work.

    try:
        response = requests.post(
            url='https://www.strava.com/api/v3/oauth/token',
            data=post_data)
        data = response.json()
    except Exception as e:
        print(f'ERROR: {str(e)}')
        return respond({'error': str(e)}, 500)

    return respond(data, 200)
