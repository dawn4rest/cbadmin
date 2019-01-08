// 진짜 file field 숨김
$('#id_profile_image').parent().css('display', 'none');


// fake btn으로 진짜 file field 클릭
$('.fake-btn').click(function () {
    $('#id_profile_image').click();
});


// 진짜 file field에서 src url 가져와서 previewHolder 변경
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#previewHolder').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    };
    $('.fake-btn h6').css('display', 'none');
}


// 진짜 file field에서 값 변경되면 함수 실행
$('#id_profile_image').change(function () {
    readURL(this);
});


// 배경 설명 3개
$('#id_background_image1').parent().css('display', 'none');
$('.fake-btn1').click(function () {
    $('#id_background_image1').click();
});
function readURL1(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#previewHolder1').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    };
    $('.fake-btn1 h6').css('display', 'none');
    $('.hide2').css('display', 'block');
}
$('#id_background_image1').change(function () {
    readURL1(this);
});


$('#id_background_image2').parent().css('display', 'none');
$('.fake-btn2').click(function () {
    $('#id_background_image2').click();
});
function readURL2(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#previewHolder2').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    };
    $('.fake-btn2 h6').css('display', 'none');
    $('.hide3').css('display', 'block');
}
$('#id_background_image2').change(function () {
    readURL2(this);
});


$('#id_background_image3').parent().css('display', 'none');
$('.fake-btn3').click(function () {
    $('#id_background_image3').click();
});
function readURL3(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#previewHolder3').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    };
    $('.fake-btn3 h6').css('display', 'none');
}
$('#id_background_image3').change(function () {
    readURL3(this);
});
