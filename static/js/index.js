$(document).on('click', '.slide-trigger', function () {
    $('#slide-menu .inner').load('/member/get_liked_posts .inner');
    $('#slide-menu').addClass('active');
});


$(document).on('click', '.slide-close', function () {
    $('#slide-menu').removeClass('active');
    $('body').css('overflow', 'auto');
});
