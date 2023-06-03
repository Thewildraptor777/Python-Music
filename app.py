import music.database
from flask import Flask, render_template, request, jsonify, json
app = Flask(__name__)

current_playlist="Slime"
playlist_data = music.database.connect(
    "localhost", "musicsite", "MGZGvCFtmGN*1OUM", "music", f"SELECT * FROM {current_playlist}")
output_playlist = []
for song in playlist_data:
    output_playlist.append(song)

text = str(output_playlist)
converted_text = text.replace("'", "\"")
#
playlist_choices= music.database.connect(
    "localhost", "musicsite", "MGZGvCFtmGN*1OUM", "music", "SHOW TABLES")
print(playlist_choices[0])
final=""
for temp in playlist_choices:
    for text in temp:
        final+=" "+text
@app.route('/')
def display_songs():
    info = converted_text

    return render_template('index.html', songs=output_playlist,info=info,choices=final)


if __name__ == '__main__':
    app.run()
