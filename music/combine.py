
from music import tracks,playlists
def create():
    destroy = open("html/player/final.html", "w")
    destroy.write("")
    destroy.close


    file = open("html/player/final.html", "a")

    top = open("html/player/template/top.html", "r")
    middle = open("html/player/template/middle.html", "r")
    bottom = open("html/player/template/bottom.html", "r")
    file.write(top.read())
    file.close()
    playlists.create()
    file = open("html/player/final.html", "a")
    file.write(middle.read())
    file.close()
    tracks.create()
    file = open("html/player/final.html", "a")
    file.write(bottom.read())
    file.close()
    top.close()
    middle.close()
    bottom.close()
