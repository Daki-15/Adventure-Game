document.addEventListener('DOMContentLoaded', function() {
    const location = document.body.getAttribute('data-location');
    if (location) {
        document.body.className = location;
    }
});
