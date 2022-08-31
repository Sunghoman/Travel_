from http import client
from random import random
import re
from flask import *
import random
import string
import os
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient("mongodb+srv://sungho:1464@cluster0.xcve6.mongodb.net/test")
db = client.sungho

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("index.html")

@app.route("/post_list")
def post():
  return render_template("post.html")


@app.route("/post", methods = ["GET","POST"])
def posts_post():
  if request.method == "POST":
    rate_receive = request.form["star_give"]
    image_receive = request.form["image_give"]
    title_receive = request.form["title_give"]
    comment_receive = request.form["comment_give"]
    username_receive = request.form["username_give"]

    doc = {
      "rate": rate_receive,
      "img": image_receive,
      "title": title_receive,
      "comment": comment_receive,
      "username": username_receive
    }

    db.gmo_gangneung_post.insert_one(doc)
    return jsonify({"msg": "포스팅 완료!"})

  elif request.method == "GET":
      all_post = list(db.gmo_gangneung_post.find({}, {"_id": False}))
      return jsonify({"posts": all_post})

  
@app.route("/detail")
def detail():
  return render_template("상세페이지.html")