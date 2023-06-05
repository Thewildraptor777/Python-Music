from music import database
from flask import Flask, render_template, request

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

playlist_choices= database.connect(
    "localhost", "musicsite", "MGZGvCFtmGN*1OUM", "music", "SHOW TABLES")
#print(playlist_choices[0])
final=""
for temp in playlist_choices:
    for text in temp:
        final+=text+"  "
@app.route('/')
def display_site():
    info = converted_text
    return render_template('index.html', songs=output_playlist, info=info,choices=final)

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

if __name__ == '__main__':
    app.run()
