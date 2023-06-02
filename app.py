from flask import Flask
import music.combine as combine
app = Flask(__name__)


@app.route('/')
def hello():
    combine.create()
    file = open("html/player/final.html", "r")
    site = file.read()
    return site


if __name__ == '__main__':
    app.run()
