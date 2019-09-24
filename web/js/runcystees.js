function ajaxCall(id) {
    var url = "https://4elwjwr536.execute-api.ap-south-1.amazonaws.com/runcystees/showteedesc";
    var result = null;
    var obj = new Object();
    obj.id = id;

    var jsonObj = JSON.stringify(obj);

        $.ajax({
            url: url,
            headers: {"Content-Type": "application/json"},
            type: 'POST',
            data: jsonObj,
            dataType: 'json',
            async: false,
            success: function(result)
            {
                if(result['result']===true)
                {
                    $('#quickview_desc p').html(result['desc']);
                }
                else {
                    console.log("error in call");
                }
            }
        });
}

$("#desc1").click(function(){
    ajaxCall(1);
})

$("#desc2").click(function(){
    ajaxCall(2);
})

$("#desc3").click(function(){
    ajaxCall(3);
})

$("#desc4").click(function(){
    ajaxCall(4);
})

$("#desc5").click(function(){
    ajaxCall(5);
})

$("#desc6").click(function(){
    ajaxCall(6);
})

$("#desc7").click(function(){
    ajaxCall(7);
})

$("#desc8").click(function(){
    ajaxCall(8);
})

$("#desc9").click(function(){
    ajaxCall(9);
})

$("#desc10").click(function(){
    ajaxCall(10);
})

$("#desc11").click(function(){
    ajaxCall(11);
})

$("#desc12").click(function(){
    ajaxCall(12);
})
