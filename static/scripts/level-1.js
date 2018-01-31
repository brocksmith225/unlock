$("navbar ul li").click(function() {
    $("navbar ul li").removeClass("active");
    $(this).addClass("active");
    $(".email").removeClass("email-full");
    $("#email-display").removeClass();
    $("#email-display").addClass($(this).attr("data-category"));
});

$(".star-toggle").click(function() {
    if ($(this).parent().hasClass("email-starred")) {
        $(this).parent().removeClass("email-starred");
    } else {
        $(this).parent().addClass("email-starred");
    }
    event.stopPropagation();
});

$(".email").click(function() {
    $(this).addClass("email-full");
    $(this).children("h3").before($(this).children("h2"));
    $(".exit-button").show();
});

$(".exit-button").click(function() {
    $(".email").removeClass("email-full");
    $(this).children("h3").after($(this).children("h2"));
    $(".exit-button").hide();
    event.stopPropagation();
});