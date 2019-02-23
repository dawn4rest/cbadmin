$(document).ready(function () {
    $('#id_category option:first').text('카테고리를 선택하세요.');
    $('.clearfix .control-btn').bind('click', false);
});


$('#id_title').on('input', function () {
    $('#title_count').text($(this).val().length);
    if ($(this).val().length > 7) {
        $('.nextTo2').removeClass('btn-gray');
        $('.nextTo2').addClass('btn-fill');
        $('.nextTo2').unbind('click', false);
    } else {
        $('.nextTo2').bind('click', false);
        $('.nextTo2').removeClass('btn-fill');
        $('.nextTo2').addClass('btn-gray');
    }
});


$('#id_background').keyup(function () {
    $('#background_count').text($(this).val().length);
    if ($(this).val().length > 49) {
        $('.nextTo3').removeClass('btn-gray');
        $('.nextTo3').addClass('btn-fill');
        $('.nextTo3').unbind('click', false);
    } else {
        $('.nextTo3').bind('click', false);
        $('.nextTo3').removeClass('btn-fill');
        $('.nextTo3').addClass('btn-gray');
    }
});


$('#id_pro_title').on('input', function () {
    $('#pro_title_count').text($(this).val().length);
    if (($('#id_pro_title').val().length > 3) && ($('#id_con_title').val().length > 3)) {
        $('.nextTo4').removeClass('btn-gray');
        $('.nextTo4').addClass('btn-fill');
        $('.nextTo4').unbind('click', false);
    } else {
        $('.nextTo4').bind('click', false);
        $('.nextTo4').removeClass('btn-fill');
        $('.nextTo4').addClass('btn-gray');
    }
});


$('#id_con_title').on('input', function () {
    $('#con_title_count').text($(this).val().length);
    if (($('#id_pro_title').val().length > 3) && ($('#id_con_title').val().length > 3)) {
        $('.nextTo4').removeClass('btn-gray');
        $('.nextTo4').addClass('btn-fill');
        $('.nextTo4').unbind('click', false);
    } else {
        $('.nextTo4').bind('click', false);
        $('.nextTo4').removeClass('btn-fill');
        $('.nextTo4').addClass('btn-gray');
    }
});


$('#id_category').change(function () {
    $('#id_tag').on('input', function () {
        if ($(this).val().length > 0) {
            $('.last').prop('disabled', false);
            $('.last').removeClass('btn-gray');
            $('.last').addClass('btn-fill');
            $('.last').unbind('click', false);
        }
    });
});


$('#id_tag').on('input', function () {
    if ($(this).val().length > 0) {
        $('#id_category').change(function () {
            $('.last').prop('disabled', false);
            $('.last').removeClass('btn-gray');
            $('.last').addClass('btn-fill');
            $('.last').unbind('click', false);
        });
    };
});