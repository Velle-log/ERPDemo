$(document).ready(function(){
  setTimeout(function(){
    $('.message').fadeOut(2000, function(){
      $('.main-menu').animate({
        bottom: '+=40'
      }, 500);
    });
  }, 2000);
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
      url: '/leave/apply',
      success: function(data){
        $('#content').html(data);
      },
      error: function(error){
        alert('Error:\n' + error);
      },
    });
  });

var done = "<div class='bs-example'><div class='alert alert-success fade in'><a href='#' class='close' data-dismiss='alert'>&times;</a><strong>Success!</strong>"
var done2 = " </div></div>"
  $(document).on('click', '#approve' ,function(event){
      var element = $(this);
      $.ajax({
        type: 'get',
        // url: '/leave/approve/'+$(this).attr('data'),
        url: '/leave/process_request/' + $(this).attr('data') + '/?action=accept',
        success: function(data){
          $('#request-box-'+element.attr('data')).html(done+data+done2);
        },
        error: function(error){
          alert('Error:\n' + error);
        },
      });
    });

  $(document).on('click', '#reject' ,function(event){
      var element = $(this);
      $.ajax({
        type: 'get',
        // url: '/leave/reject/'+$(this).attr('data'),
        url: '/leave/process_request/' + $(this).attr('data') + '/?action=reject',
        success: function(data){
          $('#request-box-'+element.attr('data')).html(done+data+done2);
        },
        error: function(error){
          alert('Error:\n' + error);
        },
      });
    });

  $(document).on('click', '#forward' ,function(event){
      var element = $(this);
      $.ajax({
        type: 'get',
        // url: '/leave/forward/'+$(this).attr('data'),
        url: '/leave/process_request/' + $(this).attr('data') + '/?action=forward',
        success: function(data){
          $('#request-box-'+element.attr('data')).html(done+data+done2);
        },
        error: function(error){
          alert('Error:\n' + error);
        },
      });
    });

  // $(document).on('click', '#apply', function(e){
  //   e.preventDefault();
  //   data = {
  //     type_of_leave: $('#id_type_of_leave').val(),
  //     start_date: $('#id_start_date').val(),
  //     end_date: $('#id_end_date').val(),
  //     replacing_user: $('#id_replacing_user').val(),
  //     purpose: $('#id_purpose').val(),
  //     leave_address: $('#id_leave_address').val(),
  //     csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]')[0].val(),
  //   }
  // });
});
