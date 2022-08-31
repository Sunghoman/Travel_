from http import client
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

@app.route("/post")
def post():
  return render_template("post.html")


@app.route("/posts", methods = ["GET"])
def posts_get():
  post_list = list(db.gmo.find({}, {"_id": False}))
  return jsonify({"posts": post_list})

@app.route("/posts", methods = ["POST"])
def posts_post():
  rate_receive = request.form["rate_give"]
  img_receive = request.form["img_give"]
  title_receive = request.form["title_give"]
  comment_receive = request.form["comment_give"]
  username_receive = request.form["username_give"]

  doc = {
    "rate": rate_receive,
    "img": img_receive,
    "title": title_receive,
    "comment": comment_receive,
    "username": username_receive
  }

  db.gmo_gangneung_post.insert_one(doc)
  return jsonify({"msg": "저장 완료"})
  
@app.route("/detail")
def detail():
  return render_template("상세페이지.html")