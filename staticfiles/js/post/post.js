$(document).ready(function () {
    // CHNAGE REPORT REASEON LABEL COLOR BY CHECKED
    $('input:checkbox').change(function () {
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
});
