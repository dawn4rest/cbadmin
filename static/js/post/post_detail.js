$(document).ready(function () {
    // CHECK MY PRO COMMENT EXIST TO SHOW DIVIDER OR NOT
    if ($('.pro-mine').length) {
        $('.pro-divider').css('display', 'flex');
    } else {
        $('.pro-divider').css('display', 'none');
    };

    // CHECK MY CON COMMENT EXIST TO SHOW DIVIDER OR NOT
    if ($('.con-mine').length) {
        $('.con-divider').css('display', 'flex');
    } else {
        $('.con-divider').css('display', 'none');
    };
});

// CHNAGE REPORT REASEON LABEL COLOR BY CHECKED
$('input:checkbox').change(function () {
    if ($(this).is(':checked')) {
        $(this).parent().css('color', '#3d3d3d');
    } else {
        $(this).parent().css('color', '#C3C5C7');
    }
});
