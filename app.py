from flask import Flask
import tracks.combine as combine
app = Flask(__name__)


@app.route('/')
def hello():
    combine.run()
    file = open("html/player/final.html", "r")
    site = file.read()
    return site


if __name__ == '__main__':
    app.run()
