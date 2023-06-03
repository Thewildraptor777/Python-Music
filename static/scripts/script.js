const tracksList = document.getElementById("playlist-tracks");
const tracks = tracksList.getElementsByTagName("li"); const total = document.getElementById("total-songs");
const playButtonDiv = document.getElementById("play-button-div"); const pauseButtonDiv = document.getElementById("pause-button-div");
const playButton = document.getElementById("play-button"); const pauseButton = document.getElementById("pause-button");
const audio = document.getElementById("audio");
let curentIndex = 0
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
   // document.getElementById("title").innerHTML=playlistData[curentIndex][3]

    if (shuffle == true) {
        let randIndex = Math.floor(Math.random() * playlistData.length);
        curentIndex = randIndex
        audio.src = links[curentIndex]

    } else {


        curentIndex++
        audio.src = links[curentIndex]
    }    
    document.getElementById("title").innerHTML= playlistData[curentIndex][3];
    document.getElementById("artist").innerHTML= playlistData[curentIndex][4];
    document.getElementById("music-image").src= playlistData[curentIndex][2];

}
audio.onended = () => {
    next();
};

audio.addEventListener('loadedmetadata', function () {
    var duration = audio.duration;
    //console.log(duration)
        
    const minutes = Math.floor(duration / 60);
    const seconds = Math.floor(duration % 60);
    //console.log(seconds)
    let final=minutes.toString()+"."+seconds.toString()
    //console.log(final);
    

    document.getElementById("length").innerHTML = "Length:" + final;
    document.getElementById("title").innerHTML= playlistData[curentIndex][3];
    document.getElementById("artist").innerHTML= playlistData[curentIndex][4];
    document.getElementById("music-image").src= playlistData[curentIndex][2];
});
