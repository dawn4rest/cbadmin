$(document).on('click', '.slide-trigger', function () {
    $('#slide-menu .inner').load('/member/get_liked_posts #slide-menu .inner');
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
        color: '#fff',
        opacity: '0.8',
        backgroundColor: 'rgb(0,0,0)',
        animation: 'fadingCircle'
    });
}