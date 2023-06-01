import tracks.data as data



playlist = []
for x in data.myresult:
  playlist.append(x)
destroy=open("html/player/final.html","w")
destroy.write("")
destroy.close
file=open("html/player/final.html","a")


top=open("html/player/template/top.html","r")
bottom=open("html/player/template/bottom.html","r")
file.write(top.read())
for track in playlist:
    output ="<li>"+"<img src='"+ track[2] +"'>"+"<p>"+ track[3]+"</p>"+"<p>" + track[4]+"</p>"+"</li>"
    file.write(output+"\n")
file.write(bottom.read())
file.close()
top.close()
bottom.close()
data.mydb.close()
data.mycursor.close()