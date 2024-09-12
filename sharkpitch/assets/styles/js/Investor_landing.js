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

document.addEventListener('DOMContentLoaded', function() {
    const searchBar = document.getElementById('search-bar');

    if (searchBar) {
        searchBar.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const videos = document.querySelectorAll('.video-item');

            videos.forEach(function(video) {
                const videoName = video.querySelector('.video-name').textContent.toLowerCase();

                if (videoName.includes(searchTerm)) {
                    video.style.display = '';
                } else {
                    video.style.display = 'none';
                }
            });
        });
    } 
});


const categoryButtons = document.querySelectorAll('li.category');
const videos = document.querySelectorAll('#clickable-video');

categoryButtons.forEach(button => { 
    button.addEventListener('click', function() {
        const selectedCategory = this.getAttribute('data-category');
        console.log('Selected category:', selectedCategory);

        videos.forEach(video => {
            const videoCategory = video.getAttribute('data-tag').toLowerCase();
            if (videoCategory === selectedCategory || selectedCategory === 'all') {
                video.style.display = ''; 
            } else {
                video.style.display = 'none';
            }
        });
    });
});
