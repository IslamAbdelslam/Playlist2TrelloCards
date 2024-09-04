#Convert-youtube-playlist-to-Trello-list

import requests

# YouTube and Trello API credentials
youtube_api_key = 'YOUR_YOUTUBE_API_KEY'
trello_api_key = 'YOUR_TRELLO_API_KEY'
trello_token = 'YOUR_TRELLO_TOKEN'

# Trello board and list IDs
trello_board_id = 'YOUR_TRELLO_BOARD_ID'
trello_list_id = 'YOUR_TRELLO_LIST_ID'

# YouTube playlist ID
playlist_id = 'YOUR_YOUTUBE_PLAYLIST_ID'

# Function to get all videos in a YouTube playlist


def get_playlist_videos(playlist_id, youtube_api_key):
    base_url = 'https://www.googleapis.com/youtube/v3/playlistItems'
    videos = []
    next_page_token = None

    while True:
        params = {
            'part': 'snippet',
            'playlistId': playlist_id,
            'maxResults': 50,
            'pageToken': next_page_token,
            'key': youtube_api_key
        }
        response = requests.get(base_url, params=params).json()
        videos.extend(response['items'])
        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break

    return videos

# Function to create Trello cards


def create_trello_card(card_name, card_desc, trello_api_key, trello_token, trello_list_id):
    url = f"https://api.trello.com/1/cards"
    query = {
        'name': card_name,
        'desc': card_desc,
        'idList': trello_list_id,
        'key': trello_api_key,
        'token': trello_token
    }
    response = requests.post(url, params=query)
    return response.json()


# Fetch videos from the playlist
videos = get_playlist_videos(playlist_id, youtube_api_key)

# Create a Trello card for each video
for video in videos:
    title = video['snippet']['title']
    url = f"https://www.youtube.com/watch?v={
        video['snippet']['resourceId']['videoId']}"
    description = f"Watch this video: {url}"
    create_trello_card(title, description, trello_api_key,
                       trello_token, trello_list_id)

print("All videos have been added as Trello cards!")
