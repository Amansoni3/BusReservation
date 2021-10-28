$(document).ready(function () {

    $.getJSON('/fetchcityjason',function(data) {

        $.each(data,function (index,item) {

            $('#source').append($('<option>').text(item[1]).val(item[0]))

        })
    })

    $.getJSON('/fetchcityjason',function(data) {

        $.each(data,function (index,item) {

            $('#destination').append($('<option>').text(item[1]).val(item[0]))

        })
    })





$('#picture').change(function () {
    var file=picture.files[0]
    pic.src=URL.createObjectURL(file)
})


})