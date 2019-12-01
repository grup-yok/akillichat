$(document).ready(function(){
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    var usertmp = '<div class="message message-user p-2"></div>';
    var bottmp = '<div class="message message-bot p-2"></div>';
    var messages = $('.messages');
    var question = $('#question');
    var micOpen = 'fa-microphone';
    var micClose = 'fa-microphone-alt-slash';

    var mic = false;

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
            newBottmp = $(bottmp).html("<span class='bold text-success' id='loading'> Ne dediğini anlamadım. Sorgu internette aranıyor... Sonuçlar kayıt edilecek... </span>");
            messages.append(newBottmp);
        },
        complete:function(){
            $('.messages').scrollTop($('.messages')[0].scrollHeight);
            $("#loading").remove();
        }
    });

    messages.append('<div class="message-info p-2 text-info"><span class="bold">Info: </span> Kafanıza takılan sorular varsa bana sorabilirsiniz. </div>');

    window.sendMessage = function(){
        userTmp = $(usertmp).html("<span class='bold text-danger'>Soru: </span>"+question.val());
        messages.append(userTmp);

        window.sendMessageToBackend(question.val(), function(data){
            if(data){
                botTmp = $(bottmp).html("<span class='bold text-success'>Cevap: </span>"+data.message);
                messages.append(botTmp);
            }
        });

        question.val('');
    };

    window.micOpenClose = function(){
        if(!mic){
            $('.btn-mic').find('i').removeClass(micOpen);
            $('.btn-mic').find('i').addClass(micClose);
            window.textToSpeech().start();
            mic = true;
        }else{
            $('.btn-mic').find('i').removeClass(micClose);
            $('.btn-mic').find('i').addClass(micOpen);
            window.textToSpeech().stop();
            mic = false;
        }
    }

    

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

    window.textToSpeech = function(){
        var noteContent = "";
        try {
            var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            var recognition = new SpeechRecognition();
        }
        catch(e) {
            console.log("Error:"+e);
        }

        
        recognition.lang = 'tr-TR';
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.onstart = function() { 
            console.log('Voice recognition activated. Try speaking into the microphone.');
        }
          
        recognition.onspeechend = function() {
            console.log('You were quiet for a while so voice recognition turned itself off.');
        }
          
        recognition.onerror = function(event) {
            if(event.error == 'no-speech') {
                console.log('No speech was detected. Try again.');  
            };
        }

        recognition.onresult = function(event) {

            // event is a SpeechRecognitionEvent object.
            // It holds all the lines we have captured so far. 
            // We only need the current one.
            var current = event.resultIndex;
            
            // Get a transcript of what was said.
            var transcript = event.results[current][0].transcript;
            console.log(event);
            
            // Add the current transcript to the contents of our Note.
            noteContent += transcript;
            console.log(noteContent);

            
            $('#question').val(noteContent);
            window.sendMessage();
        }

        recognition.onstop = function(){
            window.sendMessage();
        }
        
        return recognition;
    }

    window.checkKey = function (event) {
        if (event.which == 13 || event.keyCode == 13) {
            window.sendMessage();
        }
    };
    

    /* I give up!
    window.takeInput = function(options){ 
        var buttonTmp = $('<button class="" onclick=""></button>');
        var inputTmp = $('<input class="form-control" placeholder="" id="" class=""/>');
        var takeInput = $('<span class="question"></span> <span class="content"></span>');
        var bottmp = $('<div class="message message-bot p-2"></div>');
        var opt = $.extend({
            'type': 'input',
            'buttons': {
                "yes": function(){},
                "no": function(){},
            },
            'question': "",
        }, options);

        switch (opt["type"]) {
            case "input":
                inputTmp.addClass('take-input');
                takeInput.find(".question").html(opt['question']);
                takeInput.find(".content").html(inputTmp.html());
                takeInput.find()

                break;
            case "button":
                
            default:
                break;
        }
    };
    */

    $('#question').on('keypress', window.checkKey);
});