document.addEventListener("DOMContentLoaded", function() {

    // Flask message transitions
    var successFlash = document.querySelector(".flash-success");

    if (successFlash) {
        setTimeout(function() {
            successFlash.classList.add("fade-out");

            setTimeout(function() {
                successFlash.remove();
            }, 1000); // remove element 1s after the transition occurs
        }, 2000);  // trigger transition after 2s of element on screen
    }


    // Scroll to advice section
    var adviceSection = document.getElementById("advice-section");
    if (adviceSection) {
        adviceSection.scrollIntoView({ behavior: "smooth" });
    }

    // Toggle advice border
    function toggleAdviceBorder() {
        adviceElement = document.querySelector('.advice');

        if(window.innerWidth <= 768) {
            adviceElement.classList.remove('gradient-border');
        } else {
            adviceElement.classList.add('gradient-border');
        }
    }

    // Run on page load
    window.addEventListener('load', toggleAdviceBorder);

    // Run on resize
    window.addEventListener('resize', toggleAdviceBorder);

});
