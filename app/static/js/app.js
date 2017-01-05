function getCookie(name){
  var cookieValue = null;
  if (document.cookie && document.cookie != ""){
    var cookies = document.cookie.split(";");
    for (var i=0; i < cookies.length; i++){
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.lenght + 1) == (name + "=")){
        cookie.Value = decodeURIComponent(
          cookie.substring(name.length + 1)
        );
        break;
      }
    }
  }
  return cookieValue;
}

function csrfSafeMethod(method){
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = getCookie("csrftoken");

$.ajaxSetup({
  beforeSend: function(xhr, settings){
    if (!csrfSafeMethod(settings.type) && !this.crossDomain){
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});

$("button").on("click", function(event){
  event.preventDefault();
  var element = $(this);
  $.ajax({
    url : "/focus_device/",
    type : "POST",
    data : { device_id : element.attr("device-id")},
    success : function(response){
      element.html(response + " ");
    }
  });
});
