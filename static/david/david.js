
$(document).ready(function() {
    let div = "";
    $(Object.keys(functions)).each(function(index, key) {
        div += `<div key="${key}">`;
        div += `<div class="title">${key}</div>`;
        $(Object.keys(functions[key])).each(function(index, key) {
            div += `<div class="subtitle text-primary" key="${key}">${key}</div>`;
        })
        div += `</div>`;
    });
    $("#menu").html(div);

    $('.subtitle').click(function() {
        const detail = functions[$(this).parent().attr('key')][$(this).attr('key')];
        $(".subtitle").removeClass('selected');
        $(this).addClass('selected');

        $("#morpheme-suffix").text(detail['suffix']);
        $("#morpheme-description").text(detail['title']);

        let examples = "<table class='table table-hover table-bordered table-striped'>"

        $(Object.keys(detail['examples'])).each(function(index, key) {
            examples += "<tr>";
            examples += `<td>${key}</td>`;
            examples += `<td>${detail['examples'][key]}</td>`;
            examples += "</tr>";
        })

        examples += "</table>"

        $("#examples").html(examples);
    })
})