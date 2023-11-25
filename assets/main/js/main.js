
// page title appearing behind navbar start

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
// page title appearing behind navbar end




// nav burger start

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

// nav burger end


// password input to text input eye button start

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


// password input to text input eye button end


// eye button #2 start
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

// eye button #2 start



// song&album tab start

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

// song&album tab start




// play button code start
function playPause(songId) {
    const audio = document.getElementById(`audio-${songId}`);
    const button = document.getElementById(`play-pause-button-${songId}`);
    const audioPlayer = document.getElementById(`audio-player-${songId}`);
    let volumeSlider = document.querySelector(`#volume-control-${songId}`);
    volumeSlider.addEventListener("change", function (e) {
        audio.volume = e.currentTarget.value / 100;
    })
    //

    let seekSlider = document.querySelector(`#seekslider-${songId}`);


    let isDragging = false;


    audio.addEventListener('timeupdate', function () {
        seekSlider.value = (audio.currentTime / audio.duration) * 100;
    });

    if (audio.paused) {
        audio.play();
        button.classList.remove('bi-play-fill');
        button.classList.add('bi-pause-fill');
        audioPlayer.classList.add('playing')
        seekSlider.style.display = "block"
        volumeSlider.style.display = "block";
    } else {
        audio.pause();
        button.classList.remove('bi-pause-fill');
        button.classList.add('bi-play-fill');
        audioPlayer.classList.remove('playing');
        seekSlider.style.display = "none"
        volumeSlider.style.display = "none";

    }
}


var video = document.getElementById("myVideo");
video.volume = 0.02
// Get the button
var btn = document.getElementById("myBtn");

// Pause and play the video, and change the button text
function myFunction() {
  if (video.paused) {
    video.play();
    btn.classList.remove('bi-play-fill');
    btn.classList.add('bi-pause-fill');
  } else {
    video.pause();
    btn.classList.remove('bi-pause-fill');
    btn.classList.add('bi-play-fill');
  }
}

var btn1 = document.getElementById('myBtnUnmute')

function unMute() {

    if (video.muted){
        video.muted = !video.muted
        btn1.classList.remove('bi-volume-mute-fill')
        btn1.classList.add('bi-volume-up-fill')

    }
    else {
        video.muted = !video.muted
        btn1.classList.remove('bi-volume-up-fill')
        btn1.classList.add('bi-mute-fill')
    }
}

