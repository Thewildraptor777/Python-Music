let playlistTracks = document.getElementsByTagName('li');
console.log(playlistTracks);


for (let i = 0; i < playlistTracks.length; i++) {
  playlistTracks[i].addEventListener("click", function () {
    currentIndex = i;
    console.log("Clicked track index:", currentIndex);
    audio.src = links[currentIndex];
    audio.play()
    pauseButtonDiv.classList.remove("clear")
    playButtonDiv.classList.add("clear")
    out = false
    updateInfo()
  });
}
