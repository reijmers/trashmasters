from googleapiclient.discovery import build

# Replace with your API key
API_KEY = 'AIzaSyC6R9O6OdwhFCbJaEjVkDzYOTUJpYGkrQE'

youtube = build('youtube', 'v3', developerKey=API_KEY)

# Search for videos
search_response = youtube.search().list(
    q='afvalwijzer Amsterdam',
    type='video',
    part='id,snippet',
    maxResults=4,
    order='relevance'  # Sort by relevance
).execute()

# Extract video links
video_data = []
for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
        link = f'https://www.youtube.com/watch?v={search_result["id"]["videoId"]}'
        video_data.append({'link': link})

# You can skip the sorting step, as the results are already sorted by relevance
for video in video_data:
    print(video['link'])