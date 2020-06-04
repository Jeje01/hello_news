import requests
from flask import Flask, render_template, request, redirect
from scrapper import get_news

base_url = "http://hn.algolia.com/api/v1"

new = f"{base_url}/search_by_date?tags=story"

popular = f"{base_url}/search?tags=story"


def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

@app.route("/")
def home():
  ref = request.args.get('order_by')
  if ref=="popular" or ref is None:
    popularNews = db.get("popular")
    if popularNews:
      news = popularNews
    else:
      news = get_news(popular)
      db["popular"] = news
    return render_template("index.html", url=base_url, news=news)
  elif ref=="new":
    newNews = db.get("new")
    if newNews:
      news = newNews
    else:
      news = get_news(new)
      db["new"] = news
    return render_template("new.html", url=base_url, news=news)

app.run(host="0.0.0.0")