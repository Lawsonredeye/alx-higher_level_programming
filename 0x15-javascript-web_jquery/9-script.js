$( document ).ready(function(){
  $.ajax({
    method: "GET",
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    dataType: "json"
  }).done(function(data){
    console.log(data.hello);
    $("#hello").text(data.hello)
  })
})