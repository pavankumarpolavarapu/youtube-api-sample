import argparse
from pprint import pprint
from googleapiclient.discovery import build

def get_data(key: str, channel: str) -> int:
    youtube = build('youtube', 'v3', developerKey=key)

    #request = youtube.channels().list(part='contentDetails',forUsername=channel)
    request = youtube.playlistItems().list(part='status', playlistId='UUyXi7LITsjtfK1ugNTnsBpg')
    response = request.execute()

    pprint(response)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('channel', default='')
    args = parser.parse_args()
    api_key = ''
    with open('.env') as f:
        lines = f.read().splitlines()
        for line in lines:
            line = line.strip()
            key, value = line.split("=", maxsplit=1)
            if key == 'api_key':
                api_key = value

    get_data(api_key, args.channel)
    return 0


if __name__ == '__main__':
    SystemExit(main())
