$(document).ready(function(){
  setTimeout(function(){
    $('.message').fadeOut(2000, function(){
      $('.main-menu').animate({
        bottom: '+=40'
      }, 500);
    });
  }, 2000);
  $('input').each(function(idx){
    if($(this).attr('name') === 'remember'){
        return;
    }
    $(this).addClass('form-control');
  });
});


