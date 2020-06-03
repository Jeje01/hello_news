import requests
from flask import Flask, render_template, request, redirect
from scrapper import get_news

base_url = "http://hn.algolia.com/api/v1"

new = f"{base_url}/search_by_date?tags=story"

popular = f"{base_url}/search?tags=story"


def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("HelloNews")

@app.route("/")
def home():
  ref = request.args.get('order_by')
  if ref=="popular" or ref is None:
    get_news(popular)
    return render_template("index.html", orderBy="popular")
  elif ref=="new":
    return render_template("index.html", orderBy="new")

app.run(host="0.0.0.0")