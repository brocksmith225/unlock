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
    $(".email-full h3").after($(".email-full h2"));
    $(".email").removeClass("email-full");
    $(".exit-button").hide();
    event.stopPropagation();
});

$("#compose").click(function() {
   alert("This feature is only for B-Mail Prime. For now, please enjoy looking at your emails on our free platform. Sorry for any inconvenience and thank you for choosing B-Mail.") 
});

$(function() {
   setTimeout(function() {
       $(".large-title").hide();
   }, 666);
});