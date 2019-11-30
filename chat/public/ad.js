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
        var ask = $('#ask');

        if(question.val() !== undefined){    
            usertmp.html("Soru: "+question.val());
            messages.append(usertmp);
        }

        window.sendMessageToBackend(question.val(), function(data){
            if(data){
                bottmp.html("Cevap: "+data.message);
                messages.append(bottmp);
            }
        });


    };