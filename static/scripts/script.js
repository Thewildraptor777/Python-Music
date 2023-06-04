const tracksList = document.getElementById("playlist-tracks");
const tracks = tracksList.getElementsByTagName("li"); const total = document.getElementById("total-songs");
const playButtonDiv = document.getElementById("play-button-div"); const pauseButtonDiv = document.getElementById("pause-button-div");
const playButton = document.getElementById("play-button"); const pauseButton = document.getElementById("pause-button");
const audio = document.getElementById("audio");
let currentIndex = 0
let shuffle = false;
let loop = false;
let out = false;
playButton.addEventListener("click", () => {
    pauseButtonDiv.classList.remove("clear")
    playButtonDiv.classList.add("clear")
    audio.play()
    out = false
});
pauseButton.addEventListener("click", () => {
    playButtonDiv.classList.remove("clear")
    pauseButtonDiv.classList.add("clear")
    audio.pause()
    out = false


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
const loopIcon = document.getElementById("loop-icon");
const loopButton = document.getElementById("loop-button");
loopButton.addEventListener("click", () => {
    if (loopIcon.style.color != "red") {
        loopIcon.style.color = "red";
        loop = true;
    }
    else {
        loopIcon.style.color = 'black';
        loop = false;
    }


})
function length() {

    var duration = audio.duration;
    ////console.log(duration)

    const minutes = Math.floor(duration / 60);
    const seconds = Math.floor(duration % 60);
    ////console.log(seconds)
    let final = minutes.toString() + "." + seconds.toString()
    ////console.log(final);


    document.getElementById("length").innerHTML = "Length:" + final;
}
audio.onloadedmetadata = () => {
    length()
}

function updateInfo() {

    document.getElementById("title").innerHTML = playlistData[currentIndex][3];
    document.getElementById("artist").innerHTML = playlistData[currentIndex][4];
    document.getElementById("music-image").src = playlistData[currentIndex][2];
    document.getElementById('no-more').innerHTML = ""

}

function next() {
    // document.getElementById("title").innerHTML=playlistData[currentIndex][3]
    if (out != true) {

        if (shuffle == true) {
            let randIndex = Math.floor(Math.random() * playlistData.length);
            currentIndex = randIndex
            //console.log(currentIndex)
            audio.src = links[currentIndex]
            audio.play()

        } else {


            currentIndex++
            //console.log(currentIndex)

            audio.src = links[currentIndex]
            audio.play()

        }
        pauseButtonDiv.classList.remove("clear")
        playButtonDiv.classList.add("clear")
        audio.play()
    }
    if (loop == true) {
        let loopIndex = playlistData.length - currentIndex - 1;

        //console.log(loopIndex)
        if (loopIndex == 0) { currentIndex = -1 }
    } else if (currentIndex == playlistData.length) {
        document.getElementById("no-more").innerHTML = ("no more songs")
        out = true
    } else {
        out = false
    }
    if (out != true) {
        updateInfo()
    }
}
function prev() {
    if (currentIndex == 0) {
        out = true
        audio.pause()
        playButtonDiv.classList.remove("clear")
        pauseButtonDiv.classList.add("clear")
    }
    if (currentIndex == playlistData.length) {
        out = false
    }
    if (out == true) {  document.getElementById('no-more').innerHTML = "no more";playButtonDiv.classList.add("clear");
    pauseButtonDiv.classList.remove("clear"); } else {
        pauseButtonDiv.classList.remove("clear")
        playButtonDiv.classList.add("clear")
        audio.play()
        if (currentIndex == 0) {
            currentIndex = playlistData.length
        }
        currentIndex -= 1
        //console.log(currentIndex)
        audio.src = links[currentIndex]
        audio.play()

        updateInfo()
        out = false
    }
}
audio.onended = () => {
    next();
};

window.onload = () => {
    updateInfo()
}