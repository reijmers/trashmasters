import yt_scrape_relevance
import api_ytcomments
import googleapiclient.discovery
import googleapiclient.errors
import os
print("current working directory:", os.getcwd())


video_ids = yt_scrape_relevance.get_video_ids()
print(video_ids)

for video_id in video_ids:
    try:
        comments = api_ytcomments.gather_comments(video_id)
        if comments.empty:
            print(f"dataframe is empty for vid {video_id}")
            file_name= f'comments_{video_id}.csv.csv'
            os.remove(file_name)
            print(f"deleted empty file: {file_name}")
    except googleapiclient.errors.HttpError as e:
        if e.resp.status == 403 and "commentDisabled" in e.content.decode('utf-8'):
            print("Comments are disabled for this video. Skipping...")
        else:
            # Handle other HTTP errors as needed
            print(f"Error: {e}")

    
    print(comments.head())
