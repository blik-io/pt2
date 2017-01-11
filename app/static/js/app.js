/*
Security methods
IMPORTANT: DO NOT WORK WITH THIS SITE AFTER MANIPULATING THESE METHODS
*/
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

/*
UI methods
*/
$(".device-focus").click(function(event){
  event.preventDefault();
  var this_button=$(this);
  $.ajax({
    url : "/focus_device/",
    type : "POST",
    data : { device_id : this_button.attr("object-id")},
    success : function(focus){
      this_button.html(focus==="1" ? "Focused": "Not Focused");
    }
  });
});

$(".location-focus").click(function(event){
  event.preventDefault();
  var this_button=$(this);
  $.ajax({
    url : "/focus_device/",
    type : "POST",
    data : { location_id : this_button.attr("object-id")},
    success : function(focus){
      this_button.html(focus==="1" ? "Focused": "Not Focused");
    }
  });
});

/*
Chart methods
*/
var ctx = document.getElementById("temperature");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});
