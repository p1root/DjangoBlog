$(document).ready(function() {
    $('#login-form').submit(function(event) {
        var username = document.getElementsByName('username')[0].value
        var password = document.getElementsByName('password')[0].value
        var form_data ={
            username : username,
            password : password
        }
        event.preventDefault();
        var form_data = $(this).serialize();
        $.ajax({
            url: '{% url "login" %}',
            type: 'post',
            data: form_data,
            dataType: 'json',
            success: function(data) {
                if (data.success) {
                    window.location.href = '/';
                } else {
                    alert(data.error);
                }
            },
            error: function(xhr, errmsg, err) {
                alert(errmsg);
            }
        });
    });
});