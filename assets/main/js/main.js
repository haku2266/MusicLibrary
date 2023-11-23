// const toggleMenu = () => {
//         document.body.classList.toggle("open");
//       };


let navbarText = document.querySelector('.page-title');

window.addEventListener('scroll', function () {
    // Calculate the opacity based on the scroll position
    let opacity = 1 - window.scrollY / 150; // You can adjust the divisor for a faster or slower fade

    // Ensure opacity is between 0 and 1
    opacity = Math.min(1, Math.max(0, opacity));

    // Set the opacity of the navbar text
    navbarText.style.opacity = opacity;
});


let navbar = document.querySelector('.my-nav');
let initialColor = getComputedStyle(navbar).backgroundColor;

window.addEventListener('scroll', function () {
    // Calculate the scroll position
    let scrollPosition = window.scrollY;

    // Set a threshold for changing the background color
    let threshold = 100;

    // Change the background color based on the scroll position
    if (scrollPosition > threshold) {
        navbar.style.backgroundColor = '#000'; // Change this to your desired color
    } else {
        navbar.style.backgroundColor = initialColor;
    }
});


// Number of clicks on the trigger element initially set on 0
let numOfClicks = 0;
// Get trigger element
const trigger = document.getElementById("menu-trigger");
// Get body element
const bodyEl = document.getElementsByTagName("body")[0];

const toggleMenu = () => {
    document.body.classList.toggle("open");
    numOfClicks += 1;
    // Check if number of clicks is an even value:
    // odd value - first click, even value - second click
    const isNumOfClicksEven = numOfClicks % 2 === 0;
    // On first click set body's overflow property to "auto",
    // On second click set body's overflow property to "hidden"
    isNumOfClicksEven ? bodyEl.style.overflow = "auto" : bodyEl.style.overflow = "hidden";
};

$(document).ready(function () {
    $(".toggle-password").click(function () {
        var passwordInput = $(".password-input");

        if (passwordInput.attr("type") === "password") {
            passwordInput.attr("type", "text");
            $(".toggle-password").attr("class", "bi bi-eye-fill toggle-password position-absolute "); // Replace with your open eye icon
        } else {
            passwordInput.attr("type", "password");
            $(".toggle-password").attr("class", "bi-eye-slash-fill toggle-password position-absolute "); // Replace with your closed eye icon
        }
    });
});


$(document).ready(function () {
    $(".toggle-confirm-password").click(function () {
        var passwordInput = $(".confirm-password-input");

        if (passwordInput.attr("type") === "password") {
            passwordInput.attr("type", "text");
            $(".toggle-confirm-password").attr("class", "bi bi-eye-fill toggle-confirm-password position-absolute "); // Replace with your open eye icon
        } else {
            passwordInput.attr("type", "password");
            $(".toggle-confirm-password").attr("class", "bi bi-eye-slash-fill toggle-confirm-password position-absolute"); // Replace with your closed eye icon
        }
    });
});


const tabs = document.querySelectorAll(".my-tabs .tabs li");
const sections = document.querySelectorAll(".my-tabs .tab-content");

tabs.forEach(tab => {
    tab.addEventListener("click", e => {
        e.preventDefault();
        removeActiveTab();
        addActiveTab(tab);
    });
})

const removeActiveTab = () => {
    tabs.forEach(tab => {
        tab.classList.remove("d-block");
    });
    sections.forEach(section => {
        section.classList.remove("d-block");
    });
}

const addActiveTab = tab => {
    tab.classList.add("d-block");
    const href = tab.querySelector("a").getAttribute("href");
    const matchingSection = document.querySelector(href);
    matchingSection.classList.add("d-block");
}


// var audio = document.getElementById("myAudio");
//
// function playPause() {
//     if (audio.paused) {
//         audio.play();
//     } else {
//         audio.pause();
//     }
// }
//
// var audioPlayer = document.getElementById("play-pause-button");
// function showAudioPlayer() {
//     audioPlayer.style.display = "block";
// }
//
// function hideAudioPlayer() {
//     audioPlayer.style.display = "none";
// }


function playPause(songId) {
    const audio = document.getElementById(`audio-${songId}`);
    const button = document.getElementById(`play-pause-button-${songId}`);

    if (audio.paused) {
        audio.play();
        button.classList.remove('bi-play-fill');
        button.classList.add('bi-pause-fill');
    } else {
        audio.pause();
        button.classList.remove('bi-pause-fill');
        button.classList.add('bi-play-fill');
    }
}
//
// function showAudioPlayer(songId) {
//     var audioPlayer = document.getElementById('audio-player-${songId}');
//     audioPlayer.style.display = "block";
// }
//
// function hideAudioPlayer(songId) {
//     var audioPlayer = document.getElementById('audio-player-${songId}');
//     audioPlayer.style.display = "none";
// }