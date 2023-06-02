from flask import Flask, render_template
app = Flask(__name__)



import music.database
playlist_data=music.database.connect("localhost","Tyler","Blackrobin7","music","SELECT * FROM Slime")
output_playlist=[]
for song in playlist_data:
    output_playlist.append(song)




@app.route('/')
def display_songs():
    
    return render_template('index.html', songs=output_playlist)

if __name__ == '__main__':
    app.run()
