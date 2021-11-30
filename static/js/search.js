$(document).ready(function () {
    $("#searchInput").on('keyup', function (event) {
        let text = $(this).val();
        if (text != ''){
            $.ajax({
            url: "/api/v1/search?q="+text,
            type: "GET",
            contentType: "application/json; charset=utf-8",
            success: (elems) =>{
                $.each (elems, function (index,val) {
                    $.each(val, function(key,value){
                    if (key === 'name'){
                            $("#searchResults").append("<li>"+ value + "</li>");
                    }
                    });
                    });
                }
            });
        }
        else{
            $("#searchResults").empty();
        }
    });
});