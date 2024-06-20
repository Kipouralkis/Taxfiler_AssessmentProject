// flashes.js

document.addEventListener("DOMContentLoaded", function() {
    var successFlash = document.querySelector(".flash-success");

    if (successFlash) {
        setTimeout(function() {
            successFlash.classList.add("fade-out");

            setTimeout(function() {
                successFlash.remove();
            }, 1000); // remove element 1s after the transition occurs
        }, 2000);  // trigger transition after 2s of element on screen
    }
});
