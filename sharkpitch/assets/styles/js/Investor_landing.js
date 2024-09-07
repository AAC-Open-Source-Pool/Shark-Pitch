const videos = document.querySelectorAll('.clickable-video');
videos.forEach(video => {
    video.addEventListener('click', function() {
        if (video.paused) {
            video.play();
        } else {
            video.pause();
        }
    });
});


document.getElementById('search-bar').addEventListener('input', function() {
    const searchQuery = this.value.toLowerCase();
    const videoItems = document.querySelectorAll('.clickable-video');
    videoItems.forEach(item => {
        const startup = item.getAttribute('data-startup').toLowerCase();
        if (startup.includes(searchQuery)) {
            item.style.display = ''; 
        } else {
            item.style.display = 'none'; 
        }
    });
});
