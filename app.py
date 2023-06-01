from flask import Flask
import tracks.tracks as tracks
app = Flask(__name__)

file=open("html/player/final.html","r")
site=file.read()
@app.route('/')
def hello():
    return site

if __name__ == '__main__':
    app.run()
