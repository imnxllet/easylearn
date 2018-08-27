$( document ).ready(function() {
    //alert( "ready!" );
    $.get("../bar.html", function(html_string)
   {	

      $( "#bar" ).prepend(html_string);
   },'html'); 
});

