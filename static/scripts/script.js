const tracksList = document.getElementById("playlist-tracks");
const tracks = tracksList.getElementsByTagName("li"); const total = document.getElementById("total-songs");
const playButtonDiv = document.getElementById("play-button-div"); const pauseButtonDiv = document.getElementById("pause-button-div");
const playButton = document.getElementById("play-button"); const pauseButton = document.getElementById("pause-button");
const audio = document.getElementById("audio");
let i = 0
let shuffle = false;
playButton.addEventListener("click", () => {
    pauseButtonDiv.classList.remove("clear")
    playButtonDiv.classList.add("clear")
    audio.play()

});
pauseButton.addEventListener("click", () => {
    playButtonDiv.classList.remove("clear")
    pauseButtonDiv.classList.add("clear")
    audio.pause()

});
const shuffleIcon = document.getElementById("shuffle-icon");
const shuffleButton = document.getElementById("shuffle-button");
shuffleButton.addEventListener("click", () => {
    if (shuffleIcon.style.color != "red") {
        shuffleIcon.style.color = "red";
        shuffle = true;
    }
    else {
        shuffleIcon.style.color = 'black';
        shuffle = false;
    }


})

function next() {
    if (shuffle = true) {
        let randIndex = Math.floor(Math.random() * playlistData.length);
        i = randIndex
        audio.src = links[i]

    } else {


        i++
        audio.src = links[i]
    }
}
audio.onended = () => {
    next();
};

audio.addEventListener('loadedmetadata', function () {
    var duration = audio.duration;
    console.log(duration)
    var temp = duration / 60
    const roundedNumber = temp.toFixed(2);
    
    console.log(roundedNumber);
    

    document.getElementById("length").innerHTML = "Length:" + roundedNumber;
});
