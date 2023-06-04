import music.database
from flask import Flask, render_template, request, jsonify, json
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

global current_playlist
current_playlist = "Slime"

def update_playlist():
    global output_playlist, converted_text
    playlist_data = music.database.connect(
        "localhost", "musicsite", "MGZGvCFtmGN*1OUM", "music", f"SELECT * FROM {current_playlist}")
    output_playlist = []
    for song in playlist_data:
        output_playlist.append(song)

    text = str(output_playlist)
    converted_text = text.replace("'", "\"")

scheduler = BackgroundScheduler()
scheduler.add_job(update_playlist, 'interval', seconds=3)
scheduler.start()
playlist_choices = music.database.connect(
    "localhost", "musicsite", "MGZGvCFtmGN*1OUM", "music", "SHOW TABLES")
final = ""
for setup in playlist_choices:
    for text in setup:
        final += " " + text

@app.route('/')
def display_site():
    info = converted_text
    return render_template('index.html', songs=output_playlist, info=info, choices=final)

@app.route("/process_variable")
def process_variable():
    variable = request.args.get("variable")
    response = f"You sent: {variable}"
    return response

if __name__ == '__main__':
    app.run()
