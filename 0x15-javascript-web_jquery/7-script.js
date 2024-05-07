$( document ).ready(function() {
    $.ajax({
        url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
        dataType: "json"
    }).done(function(data){
        $("#character").append("<p>"+data.name+"</p>");
    })
})