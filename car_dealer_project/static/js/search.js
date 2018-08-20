

$(document).ready(function(){
    $('#search_rent').keyup(function() {

        $.ajax({
            type: "POST",
            url:'/search_rent',
            data:{
                'search_text':$('#search_rent').val(),
                'csfrmiddlewaretoken':$('input[name=csfrmiddlewaretoken]').val()
            },
            success: searchSuccess,
            dataType:'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR){
    $('#search-results-rent').html(data);
}


$(document).ready(function(){
    $('#search_sell').keyup(function() {

        $.ajax({
            type: "POST",
            url:'/search_sell',
            data:{
                'search_text':$('#search_sell').val(),
                'csfrmiddlewaretoken':$('input[name=csfrmiddlewaretoken]').val()
            },
            success: searchSuccess1,
            dataType:'html'
        });
    });
});

function searchSuccess1(data, textStatus, jqXHR){
    $('#search-results-sell').html(data);
}