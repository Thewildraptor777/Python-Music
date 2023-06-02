import database
playlist_data=database.connect("localhost","Tyler","Blackrobin7","music","SELECT * FROM Slime")
output_playlist=[]
for song in playlist_data:
    output_playlist.append(song[1])
print(output_playlist)