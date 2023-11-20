# gather video IDS for the most relevant youtube videos 
from googleapiclient.discovery import build
import json

API_KEY = 'AIzaSyDDkr8397Q6zUCnDTdjlFwjBzBkw_Uosi4'

youtube = build('youtube', 'v3', developerKey=API_KEY)

# Search for videos
search_response = youtube.search().list(
    q='afvalwijzer Amsterdam',
    type='video',
    part='id,snippet',
    maxResults=10,
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
       if len(video_data) == 10:
          break
       
def get_video_ids():
    return [video['vid_id'] for video in video_data]

