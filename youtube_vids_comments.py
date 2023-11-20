#Run all functions on the gathered youtube video  links, and save comments in CSV files 
import yt_scrape_relevance
import api_ytcomments
import googleapiclient.discovery
import googleapiclient.errors
import os
#print("current working directory:", os.getcwd())

video_ids = yt_scrape_relevance.get_video_ids()
final_video_id = []

for video_id in video_ids:
    try:
        comments = api_ytcomments.gather_comments(video_id)
        if comments.empty:
            #print(f"dataframe is empty for vid {video_id}")
            file_name= f'comments_{video_id}.csv'
            os.remove(file_name)
            #print(f"deleted empty file: {file_name}")
        else:
           # print(comments[['text']].head())
           final_video_id.append(video_id)
    except googleapiclient.errors.HttpError as e:
        error_content = e.content.decode('utf-8')
        if e.resp.status == 403 and "commentsDisabled" in error_content:
            print(f"comments are disabled for this video.Skipping")
        else:
            # Handle other HTTP errors as needed
            print(f"error:{e}")
            

def final_ids(final_video_id):
    return final_video_id

