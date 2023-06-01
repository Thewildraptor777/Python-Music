import data


def create():
    playlist = []
    for x in data.myresult:
        playlist.append(x)

    file = open("html/player/final.html", "a")

    for track in playlist:
        output = "<li>"+"<img src='" + \
            track[2] + "'>"+"<p>" + track[3] + \
            "</p>"+"<p>" + track[4]+"</p>"+"</li>"
        file.write(output+"\n")
    file.close()
    data.mydb.close()
    data.mycursor.close()
