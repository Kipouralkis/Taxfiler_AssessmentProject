document.addEventListener("DOMContentLoaded", function() {

    // Flash message transitions
    function handleFlashMessages() {
        var successFlash = document.querySelector(".flash-success");

        if (successFlash) {
            setTimeout(function() {
                successFlash.classList.add("fade-out");
                setTimeout(function() {
                    successFlash.remove();
                }, 1000); // Remove element 1s after the transition occurs
            }, 2000); // Trigger transition after 2s of element on screen
        }
    }

    function displayLoading() {
        var form = document.querySelector("form");
        var loading =  document.getElementById("loading");
        var adviceSection = document.getElementById("advice-section");

        function showLoading() {
            if(adviceSection){
                adviceSection.classList.add("hidden");
            }
            window.scrollTo({ top: 0, behavior: 'smooth' });
            loading.classList.remove("hidden");
            loading.classList.add("loading-visible");
            loading.scrollIntoView();
        }

        if(form) {
            form.addEventListener("submit", showLoading);
        }
    }

    function scrollToAdviceSection() {
        var headerHeight = document.querySelector('header').offsetHeight + 100;
        var adviceSection = document.getElementById("advice-section");

        var scrollOptions = {
            behavior: 'smooth',
            block: 'start',
            // Adjusting the top margin to offset the header height
            // Ensures the top of the advice section stops just below the header
            inline: 'nearest',
            marginBlockStart: headerHeight + 'px'
        }

        if (adviceSection && !adviceSection.classList.contains('hidden')) {
            adviceSection.scrollIntoView(scrollOptions);
        }
    }

    // Initialize functions on page load
    function init() {
        handleFlashMessages();
        displayLoading();
        scrollToAdviceSection();
    }

    // Run initialization on DOMContentLoaded
    init();

})