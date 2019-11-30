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


    window.sendMessage = function(){
        var usertmp = $('<div class="message message-user"></div>');
        var bottmp = $('<div class="message message-bot"></div>');

        var messages = $('.messages');
        var question = $('#question');


        if(question.val() !== undefined){    
            usertmp.html(question.val());
            messages.append("Soru: "+question.val());
        }

        window.sendMessageToBackend(question.val(), function(data){
            if(data){
                bottmp.html(data.message);
                messages.append("Cevap: "+bottmp);
            }
        });


    };

    

    window.sendMessageToBackend = function(message, success){
        $.ajax({
            type: 'POST',
            data: {
                message: message,
            },
            url: '/api/ask',
            success: success
        });
    };

});