$(document).on('submit', '#post-form', function(event){
    event.preventDefault(); // This prevents to reload the page when hit submit.

    $.ajax({
        type: 'POST',
        url: '/create',
        data: {
            link: $('#link').val(),
            alias: $('#alias').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(data){
            $('#shorten-url').html("localhost:8000/"+data)
        }
    });
});