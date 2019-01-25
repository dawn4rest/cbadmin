$(document).ready(function () {
    $(document).on('click', '.share-trigger', function () {
        $('#shareModal .modal-content').empty();
        $('.fixed-share .share-sns').clone().appendTo('#shareModal .modal-content');
    });


    $('.report-form input:checkbox').change(function () {
        if ($(this).is(':checked')) {
            $(this).parent().css('color', '#3d3d3d');
        } else {
            $(this).parent().css('color', '#C3C5C7');
        }
    });

    $('.info-btn').click(function () {
        if ($(this).hasClass('collapsed')) {
            $(this).children('span').text('방 정보 접기');
            $(this).children('img').css('transform', 'rotate(180deg)');
        } else {
            $(this).children('span').text('방 정보 펼치기');
            $(this).children('img').css('transform', 'rotate(0deg)');
        };
    });

    $('.pro-chart').easyPieChart({
        barColor: '#41cc90',
        scaleColor: false,
        size: 80,
        animate: 1000,
        lineWidth: 8,
        onStep: function (value) {
            this.$el.find('span').text(Math.round(value));
        },
        onStop: function (value, to) {
            this.$el.find('span').text(Math.round(to));
        }
    });

    $('.con-chart').easyPieChart({
        barColor: '#FF725C',
        scaleColor: false,
        size: 80,
        animate: 1000,
        lineWidth: 8,
        onStep: function (value) {
            this.$el.find('span').text(Math.round(value));
        },
        onStop: function (value, to) {
            this.$el.find('span').text(Math.round(to));
        }
    });

    $(document).on('click', '.plzLogin', function () {
        $('.toast .content').html('<p>의견을 남기시려면 로그인이 필요해요.</p>');
        $('.toast').toast('show');
    });

    $(document).on('click', '.comment-toggle', function () {
        $('html, body').animate({
            scrollTop: $(this).offset().top
        }, 1000);
    });

    $(document).on('click', '.coc-toggle', function () {
        if ($(this).hasClass('collapsed')) {
            $(this).children('img').css('opacity', '.32');
            $(this).children('img').attr('src', '/static/img/icons/comment.png');
        } else {
            $(this).children('img').css('opacity', '1');
            $(this).children('img').attr('src', '/static/img/icons/comment-fill.png');
        }
    });
});
