from flask import Flask,redirect,url_for,render_template, request
import pytube
import os
import youtube_dl
import sys
import requests
import urllib.request
import wget
from django.urls import path
#ytd=YouTube(url)


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])    
def download():
    if request.method=="POST":
        url=request.form["url"]    
        downloadlink= "http://127.0.0.1:5000/static/1.mp4"         
        ydl_opts = {'format': 'best','noplaylist':True,'extract-  audio':True,}
        path = "C:/NRLDocuments/NRL/PythonScript/webflask/static/download/"        
        #path="/Users/bisharbn/downloads/"
        os.chdir(path)           
       # url="https://www.youtube.com/watch?v=c-I5S_zTwAc"
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
         ydl.download([url])                 
        
        # download the url contents in binary format
       # r = requests.get(url)
        video_name = url.split('/')[-1]
        print ("Downloading file" + video_name)      
        #url_for('static',filename='1.mp4')
        #wget.download("http://127.0.0.1:5000/static/", "1.mp4")
        #urllib.request.urlretrieve(url_for('static',filename='1.mp4'), '1.mp4') 
        #r = requests.get("http://127.0.0.1:5000/", stream = True) 
    # download started 
    #   with open("1.mp4", 'wb') as f: 
    #         for chunk in r.iter_content(chunk_size = 1024*1024): 
    #             if chunk: 
    #               f.write(chunk) 
        print("Downloading file" + downloadlink)     
        return render_template("index.html")
    else:
      return render_template("index.html")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<name>")#passing value from url
def user(name):
     return render_template("extend.html",content="name")


if __name__ == "__main__":
    app.run(debug=True)
