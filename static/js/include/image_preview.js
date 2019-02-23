// 진짜 file field 숨김
$('#id_profile_image').parent().hide();


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
    $('.fake-btn h6').hide();
}


// 진짜 file field에서 값 변경되면 함수 실행
$('#id_profile_image').change(function () {
    readURL(this);
});


// 배경 설명 5개
function loopReadURL(input, i) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#previewHolder' + i).attr('src', e.target.result);
            $('#previewHolder' + i).css('height', 'auto');
        }
        reader.readAsDataURL(input.files[0]);
    };
    $('.fake-btn' + i + ' h6').hide();
    $('.del-' + i).remove();
    $('.hide' + i).prepend('<span class="del-image del-' + i + '">&times;</span>');
    $('#background_image' + i + '-clear_id').prop('checked', false);

    var nextHide = i + 1;
    $('.hide' + nextHide).css('display', 'block');
};
function delImage(i) {
    $('#previewHolder' + i).removeAttr('src');
    $('#previewHolder' + i).css('height', '0');
    $('#id_background_image' + i).val('');
    $('.fake-btn' + i + ' h6').show();
    $('#background_image' + i + '-clear_id').prop('checked', 'checked');
    $('.del-' + i).remove();
};
for (let i = 1; i < 6; i++) {
    $('#id_background_image' + i).parent().hide();

    $('.fake-btn' + i).click(function () {
        $('#id_background_image' + i).click();
    });

    $('#id_background_image' + i).change(function () {
        loopReadURL(this, i);
    });

    $(document).on('click', '.del-' + i, function () {
        delImage(i);
    });
};

