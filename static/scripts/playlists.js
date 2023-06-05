document.getElementById("playlist-selection").innerHTML = ""
for (choice in playlistChoices) {
    document.getElementById("playlist-selection").innerHTML += `<a class="sendButton">${playlistChoices[choice]}</a>`

        + " "
}