from googleapiclient.discovery import build

# Replace with your API key
API_KEY = 'AIzaSyC6R9O6OdwhFCbJaEjVkDzYOTUJpYGkrQE'

youtube = build('youtube', 'v3', developerKey=API_KEY)

# Search for videos
search_response = youtube.search().list(
    q='afvalwijzer',
    type='video',
    part='id,snippet', 
    maxResults= 50
).execute()

# Extract video links + comment counts
video_data = []
for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
        link = f'https://www.youtube.com/watch?v={search_result["id"]["videoId"]}'
        comment_count = search_result['snippet'].get('commentCount', 'N/A')
        video_data.append({'link': link, 'commentCount': comment_count})

# Sort videos by comment count
video_data.sort(key=lambda x: int(x['commentCount']) if x['commentCount'] != 'N/A' else 0, reverse=True)

top_4_vids = [video['link'] for video in video_data[:4]]
for link in top_4_vids:
    print(link)