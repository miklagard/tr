$(document).ready(function () {
    $(".autocomplete").flexselect();
    checkEnglishTranslation();
}).on('click', '#english', function() {
    checkEnglishTranslation();
});

function checkEnglishTranslation() {
    if ($("#english").prop('checked')) {
        $(".english").css("display", "inline");
        $(".turkish").css("display", "none");
    } else {
        $(".english").css("display", "none");
        $(".turkish").css("display", "inline");
    }
}