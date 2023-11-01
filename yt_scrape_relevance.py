from googleapiclient.discovery import build
import json

API_KEY = 'AIzaSyC6R9O6OdwhFCbJaEjVkDzYOTUJpYGkrQE'

youtube = build('youtube', 'v3', developerKey=API_KEY)

# Search for videos
search_response = youtube.search().list(
    q='afvalwijzer Amsterdam',
    type='video',
    part='id,snippet',
    maxResults=20,
    order='relevance'  # Sort by relevance
).execute()

# Extract video links
video_data = []
video_id = []
for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
       vid_id = search_result["id"]["videoId"]
       link = f'https://www.youtube.com/watch?v={search_result["id"]["videoId"]}'
       video_data.append({'link': link, 'vid_id': vid_id})
       if len(video_data) == 20:
          break
       
def get_video_ids():
    return [video['vid_id'] for video in video_data]

