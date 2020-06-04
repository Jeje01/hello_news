import requests
import json

def get_news(url):
  response = json.loads(requests.get(url).text)["hits"]
  #title, url, points, author, num_comments
  news = []
  for item in response:
    title = item["title"]
    url = item["url"]
    points = item["points"]
    author = item["author"]
    comments = item["num_comments"]
    object_id = item["objectID"]
    news.append({"title":title, "url":url, "points":points, "author":author, "comments":comments, "object_id":object_id})
  return news