const Videos = document.querySelectorAll('.clickable-video');
Videos.forEach(video => {
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
        } 
        else {
            item.style.display = 'none';
        }
    });
});


const categoryButtons = document.querySelectorAll('.category');
const videos = document.querySelectorAll('.clickable-video');

categoryButtons.forEach(button => {
    button.addEventListener('click', function() {
        const selectedCategory = this.getAttribute('data-category');

        videos.forEach(video => {
            const videoCategory = video.getAttribute('data-tag').toLowerCase();
            if (videoCategory === selectedCategory) {
                video.style.display = ''; 
            } else {
                video.style.display = 'none';
            }
        });
    });
});
