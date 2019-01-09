$('.slide-trigger').click(function () {
    $('.slide-body').load('/member/get_liked_posts .slide-body');
    $('#slide-menu').addClass('active');
});

$('.slide-close').click(function () {
    $('#slide-menu').removeClass('active');
});
