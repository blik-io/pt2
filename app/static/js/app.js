function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
  beforeSend: function(xhr, settings){
    if (!csrfSafeMethod(settings.type) && !this.crossDomain){
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});

$("button").click(function(event){
  event.preventDefault();
  var this_button=$(this);
  $.ajax({
    url : "/focus_device/",
    type : "POST",
    data : { device_id : this_button.attr("device-id")},
    success : function(focus){
      this_button.html(focus==="1" ? "Focused": "Not Focused");
    }
  });
});
