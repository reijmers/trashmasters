import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd

api_service_name = "youtube"
api_version = "v3"
developer_key = "AIzaSyDBdG532iD4u7pXvdsM5YVXX3o4O8nKtYw" 

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=developer_key
)

video_id = "0JtoSafhvLM"
max_results = 1000
comments = []

next_page_token = None
while True:
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        pageToken=next_page_token
    )
    
    response = request.execute()
    
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([
            comment['authorDisplayName'],
            comment['publishedAt'],
            comment['updatedAt'],
            comment['likeCount'],
            comment['textDisplay']
        ])
    
    if 'nextPageToken' in response:
        next_page_token = response['nextPageToken']
    else:
        break

df = pd.DataFrame(comments, columns=['author', 'published_at', 'updated_at', 'like_count', 'text'])
print(df)
df.to_csv('comments.csv', index=False)