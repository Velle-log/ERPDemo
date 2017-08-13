$(document).ready(function(){
  $('input').each(function(idx){
    if($(this).attr('name') === 'remember'){
        return;
    }
    $(this).addClass('form-control');
  });
});
