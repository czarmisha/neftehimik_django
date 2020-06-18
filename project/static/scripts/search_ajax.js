function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
$('#post-form').on('input', function(event){
    event.preventDefault();
    console.log("form submitted!");
    if($('#post-text').val() == '')$('.result').empty();
    else {
        $('.result').empty();
        create_post();
    }
});

function create_post() {
console.log("create");
    $.ajax({
        url : "/search/",
        type : "POST",
        data : { search : $('#post-text').val() },
        success : function(json) {
            for(i=0;i<json.results.length;i++){
                $('<a>', { href: '/products/detail/'+json.results[i].pk, class:'search-a', text: json.results[i].name, style: 'display:block'}).appendTo('.result');
                console.log(json.results[i]);
            }
            console.log(json);
            console.log("success");
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
};