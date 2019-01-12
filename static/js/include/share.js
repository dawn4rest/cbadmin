// FACEBOOK SHARE
function shareFacebook() {
    window.open(
        'https://www.facebook.com/sharer/sharer.php?u='
        + encodeURIComponent(document.URL)
        + '&t='
        + encodeURIComponent(document.title),
        'facebooksharedialog',
        'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600'
    );

}


// NAVER SHARE
function shareNaver() {
    window.open(
        'https://share.naver.com/web/shareView.nhn?url='
        + encodeURIComponent(document.URL)
        + '&title='
        + encodeURIComponent(document.title),
        'naversharedialog', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=600,width=600'
    );
}


// KAKAO SHARE
Kakao.init('6fba63cdc271830b836d5f9bce148f71');
function shareKatalk() {
    Kakao.Link.sendScrap({
        requestUrl: location.href
    });
};


// COPY URL
function shareLink() {
    /* Get the text field */
    var copyText = document.getElementById("linkInput");
    copyText.value = window.location.href
    /* Select the text field */
    copyText.select();
    /* Copy the text inside the text field */
    document.execCommand("copy");
    /* Alert the copied text */
    $('.toast .content').html('<p>링크가 복사되었어요.</p><p>익명으로 자유롭게 공유하세요.</p>');
    $('.toast').toast('show');
}
