// CHNAGE REPORT REASEON LABEL COLOR BY CHECKED
$('input:checkbox').change(function () {
    if ($(this).is(':checked')) {
        $(this).parent().css('color', '#3d3d3d');
    } else {
        $(this).parent().css('color', '#C3C5C7');
    }
});
