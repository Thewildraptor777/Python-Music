from music import database
from flask import Flask, render_template, request, send_file,url_for,redirect
import pygame
import os
app = Flask(__name__)

current_playlist = "Slime"
output_playlist = []  # Initialize the variable here
converted_text = ""
stored_variable = ""  # Define stored_variable here
stored_variable = current_playlist


def update_playlist():
    global output_playlist, converted_text
    playlist_data = database.connect(
        "localhost", "musicsite", "MGZGvCFtmGN*1OUM", "music", f"SELECT * FROM {current_playlist}")
    output_playlist = []
    for song in playlist_data:
        output_playlist.append(song)

    text = str(output_playlist)
    converted_text = text.replace("'", "\"")
    print(stored_variable)


# Initialize the output_playlist variable before starting the application
update_playlist()

playlist_choices = database.connect(
    "localhost", "musicsite", "MGZGvCFtmGN*1OUM", "music", "SHOW TABLES")
# print(playlist_choices[0])
final = ""
for temp in playlist_choices:
    for text in temp:
        final += text+"  "


@app.route('/')
def display_site():
    info = converted_text
    return render_template('index.html', songs=output_playlist, info=info, choices=final)


@app.route("/process_variable")
def process_variable():
    global stored_variable, current_playlist
    variable = request.args.get("variable")
    stored_variable = variable
    current_playlist = stored_variable  # Update the value of current_playlist
    update_playlist()  # Call update_playlist to refresh the playlist
    response = f"You sent: {variable}"
    return response


@app.route("/retrieve_variable")
def retrieve_variable():
    global stored_variable
    return f"The stored variable is: {stored_variable}"

# Function to play audio file
def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Folder containing audio files
folder_path = 'data/audio'

@app.route('/audio/')
def index():
    audio_files = []

    # Iterate over the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp3') or filename.endswith('.wav'):
            audio_files.append(filename)

    return render_template('audio.html', audio_files=audio_files)

@app.route('/audio/play/<filename>')
def play(filename):
    file_path = os.path.join(folder_path, filename)
    play_audio(file_path)



# Set the upload folder path
UPLOAD_FOLDER = 'data/audio/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/audio/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Check if a file is included in the request
        if 'audio_file' not in request.files:
            return redirect(request.url)

        audio_file = request.files['audio_file']

        # Check if the file is empty
        if audio_file.filename == '':
            return redirect(request.url)

        # Save the file to the upload folder
        audio_file.save(os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename))

        return "file uploaded"+'<script>console.log("Before the delay");setTimeout(function() {console.log("After 1 second");window.location.replace("")},1000);</script>'

    return render_template('submit.html')

if __name__ == '__main__':
    app.run()
