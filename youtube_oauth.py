import argparse
import os
from pprint import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

def get_credentials() -> object:
    if os.path.exists('token.pickle'):
        print('Loading from File...')
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                print("Refreshing Access Token...")
                credentials.refresh(Request())
    else:
        print("Fetching New Token...")
        flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=['https://www.googleapis.com/auth/youtube'])
        flow.run_local_server(port=8080, prompt="consent", authorization_prompt_message="")
        credentials = flow.credentials
        with open("token.pickle", "wb") as f:
            print("Saving Credentials for Future Use...")
            pickle.dump(credentials, f)


    return credentials

def get_data(channel: str) -> int:
    credentials = get_credentials()
    youtube = build('youtube', 'v3', credentials=credentials)

    request = youtube.channels().list(part='contentDetails',forUsername=channel)
    response = request.execute()

    pprint(response)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('channel', default='')
    args = parser.parse_args()

    get_data(args.channel)
    return 0


if __name__ == '__main__':
    SystemExit(main())
