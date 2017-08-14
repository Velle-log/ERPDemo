$(document).ready(function(){
  $('#message').fadeOut(5000);
  $('#leaverequests').on('click', function(){
    $.ajax({
      type: 'get',
      url: '/leave/getapplications',
      success: function(data){
        $('#content').html(data);
      },
      error: function(error){
        alert(error);
      },
    });
  });

  $('#applyleave').on('click', function(){
    $.ajax({
      type: 'get',
      url: '/leave/maininterface',
      success: function(data){
        $('#content').html(data);
      },
      error: function(error){
        alert('Error:\n' + error);
      }
    });
  });

});
