# YouTube2Trello

Automate the process of converting all videos in a YouTube playlist into Trello cards using Python. This script fetches videos from a specified YouTube playlist and creates corresponding cards in a Trello list, making it easy to track and manage your content.

## Features

- Automatically fetch all videos from a YouTube playlist.
- Create Trello cards with the video title and link in a specified Trello list.
- Simple to set up and use.

## Prerequisites

Before you can use this script, you'll need to have the following:

1. **Python** installed on your machine.
2. **YouTube Data API Key** from the [Google Developer Console](https://console.cloud.google.com/).
3. **Trello API Key and Token** from the [Trello Developer API Keys](https://trello.com/app-key) page.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/YouTube2Trello.git
cd YouTube2Trello
```

### 2. Install Dependencies

This script requires the `requests` library. You can install it using pip:

```bash
pip install requests
```

### 3. Get API Credentials

#### YouTube Data API Key:
- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project or select an existing one.
- Navigate to **APIs & Services** > **Library**.
- Search for "YouTube Data API v3" and enable it.
- Go to **Credentials** > **Create Credentials** > **API Key**.
- Copy your API key.

#### Trello API Key and Token:
- Visit the [Trello Developer API Keys](https://trello.com/app-key) page.
- Copy your API key.
- Generate a token by clicking the link below the API key.
- Copy your token.

### 4. Get Trello Board and List IDs

1. **Board ID**: 
   - Open your Trello board in a browser. The board ID is the string after `/b/` in the URL.
   - Example: In `https://trello.com/b/abc123xyz/my-board`, `abc123xyz` is your Board ID.

2. **List ID**:
   - Use the Trello API to get the List ID:
   - Visit: `https://api.trello.com/1/boards/BOARD_ID/lists?key=YOUR_TRELLO_API_KEY&token=YOUR_TRELLO_TOKEN`
   - Replace `BOARD_ID` with your actual board ID.

### 5. Configure the Script

Open the `youtube_to_trello.py` script and replace the placeholders with your API keys, token, and IDs:

```python
youtube_api_key = 'YOUR_YOUTUBE_API_KEY'
trello_api_key = 'YOUR_TRELLO_API_KEY'
trello_token = 'YOUR_TRELLO_TOKEN'

trello_board_id = 'YOUR_TRELLO_BOARD_ID'
trello_list_id = 'YOUR_TRELLO_LIST_ID'

playlist_id = 'YOUR_YOUTUBE_PLAYLIST_ID'
```

### 6. Run the Script

After configuration, run the script:

```bash
python youtube_to_trello.py
```

The script will fetch all videos from the specified YouTube playlist and create Trello cards with the video title and link in your selected Trello list.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of the [YouTube Data API](https://developers.google.com/youtube/v3) and [Trello API](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/) for their awesome tools.

---
