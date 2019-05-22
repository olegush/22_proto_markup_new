$(function(){
  $(".phone-mask").mask("+7(999) 999-9999");
  $('#button_error_region').click(function(open_select_region){
    open_select_region.stopPropagation();
    $('#button_navbar_toggle').click();
    $('#region').dropdown('toggle');
  });
});
