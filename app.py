from http import client
import imp
from flask import *
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient("mongodb+srv://sungho:1464@cluster0.xcve6.mongodb.net/test")
db = client.sungho

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("index.html")

@app.route("/post", methods = ["GET", "POST"])
def post():
  if request.method == "GET":
    post_list = list(db.gmo.find({}, {"_id": False}))
    return jsonify({"posts": post_list})
    
  return render_template("post.html")