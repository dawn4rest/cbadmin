$(document).on('click', '.slide-trigger', function () {
    $('#slide-menu .inner').load('/member/get_liked_posts .inner');
    $('#slide-menu').addClass('active');
});


$(document).on('click', '.slide-close', function () {
    $('#slide-menu').removeClass('active');
    $('body').css('overflow', 'auto');
});


function showModal() {
    $('body').loadingModal({
        position: 'auto',
        text: 'LOADING...',
        color: '#2699fb',
        opacity: '0.64',
        backgroundColor: 'rgb(0,0,0)',
        animation: 'fadingCircle'
    });
}