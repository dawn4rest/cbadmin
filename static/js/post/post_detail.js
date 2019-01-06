// CHNAGE REPORT REASEON LABEL COLOR BY CHECKED
$('input:checkbox').change(function () {
    if ($(this).is(':checked')) {
        $(this).parent().css('color', '#3d3d3d');
    } else {
        $(this).parent().css('color', '#C3C5C7');
    }
});

$('.percentage').easyPieChart({
    animate: 1000,
    lineWidth: 4,
    onStep: function (value) {
        this.$el.find('span').text(Math.round(value));
    },
    onStop: function (value, to) {
        this.$el.find('span').text(Math.round(to));
    }
});