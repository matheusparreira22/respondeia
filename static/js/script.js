// General JavaScript functionality

document.addEventListener('DOMContentLoaded', function() {
    // Handle the notification pop-up
    const notificationPopup = document.getElementById('notification-popup');
    const closeNotificationBtn = document.getElementById('close-notification');

    // Check if the user has already seen the notification
    const hasSeenNotification = localStorage.getItem('hasSeenNotification');

    // Show the notification after a short delay if the user hasn't seen it before
    if (!hasSeenNotification && notificationPopup) {
        setTimeout(() => {
            notificationPopup.classList.remove('hidden');
        }, 1000); // Show after 1 second
    }

    // Close the notification when the button is clicked
    if (closeNotificationBtn) {
        closeNotificationBtn.addEventListener('click', function() {
            notificationPopup.classList.add('hidden');
            // Store that the user has seen the notification
            localStorage.setItem('hasSeenNotification', 'true');
        });
    }

    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add responsive navigation toggle for mobile
    const navToggle = document.querySelector('.nav-toggle');
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            const nav = document.querySelector('nav ul');
            nav.classList.toggle('show');
        });
    }
});
