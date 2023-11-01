# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

# -*- coding: utf-8 -*-

import os
import csv
import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyDBdG532iD4u7pXvdsM5YVXX3o4O8nKtYw"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet,replies",
        order="relevance",
        videoId="0JtoSafhvLM"
    )
    response = request.execute()

    # Extract the relevant data from the response
    items = response.get("items", [])

    # Save the data in a CSV file
    with open('youtube_comments_response_test.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write the header row
        csvwriter.writerow(["Author", "Comment"])

        # Write each comment as a new row in the CSV file
        for item in items:
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            author = snippet["authorDisplayName"]
            comment = snippet["textDisplay"]
            csvwriter.writerow([author, comment])

if __name__ == "__main__":
    main()
