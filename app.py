from http import client
from flask import *
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient("mongodb+srv://sungho:1464@cluster0.xcve6.mongodb.net/?retryWrites=true&w=majority")
db = client.sungho

@app.route("/")
def home():
  return render_template("index.html")