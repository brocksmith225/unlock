$(".add-to-cart").click(function() {
    $("#cart-counter").text(parseInt($("#cart-counter").text()) + 1);
});