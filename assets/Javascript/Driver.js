$(document).ready(function () {

$('#picture').change(function () {
    var file=picture.files[0]
    pic.src=URL.createObjectURL(file)
})


})