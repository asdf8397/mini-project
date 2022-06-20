from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi

ca = certifi.where()
app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:emm05235@cluster0.umzeh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.sparta

@app.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)