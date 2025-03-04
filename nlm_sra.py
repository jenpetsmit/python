# Import all needed libraries 
# Open the URL and read the API reponse
# Identify each data point in your JSON and print it to spreadsheet
import csv
import json
import requests
api_url= "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UC0l4yG9XqYtrR4E9lpzk7Ow&key=AIzaSyAGc2RgSNPS2-kdskFyt6nN31Wi-VzzeMU&q=sra"
api_response = requests.get(api_url)
videos = json.loads(api_response.text)

with open("youtube_videos_sra.csv", "w", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["publishAt",
                        "title",
                        "description"])
    if videos.get("items") is not None:
        for video in videos.get("items"):
            video_data_row = [
                video["snippet"]["publishedAt"],
                video["snippet"]["title"],
                video["snippet"]["description"],
            ]
            csv_writer.writerow(video_data_row)
        if "nextPageToken" in videos.keys():
            next_page_url = api_url +"&pageToken="+videos["nextPageToken"]
            next_page_posts =  requests.get(next_page_url)
            videos =json.loads(next_page_posts.text)
        else:
            print("no more videos") 
            has_another_page = False


___

[Return to Portfolio Home Page](https://jenpetsmit.github.io/)
