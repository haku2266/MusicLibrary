const toggleMenu = () => {
        document.body.classList.toggle("open");
      };


let navbarText = document.querySelector('.page-title');

window.addEventListener('scroll', function() {
    // Calculate the opacity based on the scroll position
    let opacity = 1 - window.scrollY / 150; // You can adjust the divisor for a faster or slower fade

    // Ensure opacity is between 0 and 1
    opacity = Math.min(1, Math.max(0, opacity));

    // Set the opacity of the navbar text
    navbarText.style.opacity = opacity;
});

