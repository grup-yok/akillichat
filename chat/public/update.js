$(document).ready(function(){
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    window.sendData = function(data, url, success){
        $.ajax({
            type: 'POST',
            data: data,
            url: '/office/'+url+'/',
            success: success
        });

    };
    window.veriekle = function(){
        var soru = $('#soru');
        var cevap = $('#cevap');

        window.sendData({
            soru:soru.val(),
            cevap:cevap.val()}, 
            'ajax',
            function(data){
                location.reload();
            });
    }
});