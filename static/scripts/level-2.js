$(".add-to-cart").click(function() {
    $("#cart-counter").text(parseInt($("#cart-counter").text()) + 1);
});

$("#search-button").click(function() {
    $.post({
        url: "/level-2/search",
        dataType: "text",
        data: $("#search-input").serialize(),
        success: function(result) {
            console.log(result);
            result = result.replace(/'/g, '"');
            searchItems = $.parseJSON(result);
            console.log(searchItems);
            $("#items").html("");
            for (i = 0; i < searchItems.length; i++) {
                $("#items").append('<div class="item"><div class="preview-img" style="background-image: url(&quot;/static/img/nile/items/' + searchItems[i]["image"] + '&quot;);"></div><h1>' + searchItems[i]["name"] + '</h1><i class="fa fa-shopping-cart add-to-cart"></i><h2>' + searchItems[i]["price"] + '</h2></div>');
            }
        }
    });
});