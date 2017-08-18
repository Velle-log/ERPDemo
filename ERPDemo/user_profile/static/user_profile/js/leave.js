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

  $('#leaves').on('click', function(){
    $.ajax({
      type: 'get',
      url: '/leave/getleaves',
      success: function(data){
        $('#content').html(data);
      },
      error: function(error){
        alert(error);
      },
    });
  });

  var m1 = "<div class='alert alert-success message'><strong>Messages:</strong><ul><li>You recieved a new Application Request</li></ul></div>";

  window.setInterval(function(){
    $.ajax({
      type: 'get',
      url: '/leave/notifications/',
      success: function(data){
        var pdata= $('#count_applications').text();
        // console.log(pdata.parseInt() ==data.parseInt());
        if(parseInt(pdata) < parseInt(data))
        {
          $('#message-box').html(m1);
          setTimeout(function(){
            $('.message').fadeOut(2000, function(){
              $('.main-menu').animate({
                bottom: '+=40'
              }, 500);
            });
          }, 2000);
        }
        $('#count_applications').html(data);
      },
      error: function(error){
      },
    });
  }, 5000);

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

var done = "<div class='bs-example'><div class='alert alert-success fade in'><a href='#' class='close' data-dismiss='alert'>&times;</a><strong>Success!</strong> "
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

  $(document).on('click', '#delete' ,function(event){
      var element = $(this);
      $.ajax({
        type: 'get',
        // url: '/leave/forward/'+$(this).attr('data'),
        url: '/leave/process_request/' + $(this).attr('data') + '/?action=delete',
        success: function(data){
          if(data=='done')
          {
          $('#leave-box-'+element.attr('data')).html(done+data+done2);
        }
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
