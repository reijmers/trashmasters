import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
import re

api_service_name = "youtube"
api_version = "v3"
developer_key = "AIzaSyDBdG532iD4u7pXvdsM5YVXX3o4O8nKtYw" 

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=developer_key
)
def gather_comments(vid_id):
#video_id = "0JtoSafhvLM"
    max_results = 1000
    comments = []

    next_page_token = None
    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=vid_id,
            maxResults=max_results,
            pageToken=next_page_token
        )

        try:
            response = request.execute()
        except googleapiclient.errors.HttpError as e:
            if e.resp.status == 403 and "commentDisabled" in e.content.decode('utf-8'):
                print("Comments are disabled for this vide, skipping.")
            else:
                print(f"Error: {e}")
            break
        
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append([
                comment['publishedAt'],
                comment['updatedAt'],
                comment['likeCount'],
                comment['textDisplay']
            ])
    
        if 'nextPageToken' in response:
            next_page_token = response['nextPageToken']
        else:
            break



    df = pd.DataFrame(comments, columns=['published_at', 'updated_at', 'like_count', 'text'])

# Data cleaning
# 1. Remove any HTML tags and URLs from the 'text' column
    df['text'] = df['text'].apply(lambda x: re.sub(r'<.*?>|https?://\S+', '', x))

# 2. Remove leading/trailing whitespaces
    df['text'] = df['text'].str.strip()

# 3. Remove empty comments
    df = df[df['text'] != '']

# 4. Remove first comment; comment made by the channel 
    df = df.iloc[1:]

# 5. Finding key words in the comments; we can add or take the key words, i put keywords axxociated to the hypotheis
    keywords = ["recycling", "circular economy", "waste sorting", "awareness", "social norms", "convenience", "inconvenience", "amsterdam"]
    df = df[df['text'].str.lower().str.contains('|'.join(keywords))]

    filename=f'comments_{vid_id}.csv'
    df.to_csv(f'{filename}.csv', index= False)

    return df

