$(document).ready(function(){
  $('.message').fadeOut(4000, function(){
    $('.main-menu').animate({
      bottom: '+=40'
    }, 500);
  });
  $('input').each(function(idx){
    if($(this).attr('name') === 'remember'){
        return;
    }
    $(this).addClass('form-control');
  });
});
