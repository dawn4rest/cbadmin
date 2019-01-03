$( document ).ready(function() {
    $('#id_category option:first').text('카테고리를 선택하세요.');
    $('.clearfix .control-btn').bind('click', false);
    $('.nextTo3').unbind('click', false);
});


$("#id_title").keypress(function() {
    if($(this).val().length > 4) {
        $('.nextTo2').removeClass('btn-gray');
        $('.nextTo2').addClass('btn-fill');
        $('.nextTo2').unbind('click', false);
    } else {
        $('.nextTo2').bind('click', false);
        $('.nextTo2').removeClass('btn-fill');
        $('.nextTo2').addClass('btn-gray');
    }
});


$("#id_pro_title").keypress(function() {
    if( ($("#id_pro_title").val().length > 4) && ($("#id_con_title").val().length > 4) ) {
        $('.nextTo4').removeClass('btn-gray');
        $('.nextTo4').addClass('btn-fill');
        $('.nextTo4').unbind('click', false);
    } else {
        $('.nextTo4').bind('click', false);
        $('.nextTo4').removeClass('btn-fill');
        $('.nextTo4').addClass('btn-gray');
    }
});


$("#id_con_title").keypress(function() {
    if( ($("#id_pro_title").val().length > 4) && ($("#id_con_title").val().length > 4) ) {
        $('.nextTo4').removeClass('btn-gray');
        $('.nextTo4').addClass('btn-fill');
        $('.nextTo4').unbind('click', false);
    } else {
        $('.nextTo4').bind('click', false);
        $('.nextTo4').removeClass('btn-fill');
        $('.nextTo4').addClass('btn-gray');
    }
});


$("#id_category").change(function() {
    $("#id_tag").keypress(function() {
        if($(this).val().length > 0) {
            $('.last').prop("disabled", false);
            $('.last').removeClass('btn-gray');
            $('.last').addClass('btn-fill');
            $('.last').unbind('click', false);
        }
    });
});


$("#id_tag").keypress(function() {
    if($(this).val().length > 0) {
        $("#id_category").change(function() {
            $('.last').prop("disabled", false);
            $('.last').removeClass('btn-gray');
            $('.last').addClass('btn-fill');
            $('.last').unbind('click', false);
        });
    };
});
