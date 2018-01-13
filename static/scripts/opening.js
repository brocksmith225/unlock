openingPage = true;

$(window).keypress(function() {
    if (openingPage) {
        $("#main-logo").removeClass();
        $("#main-logo").addClass("main-logo-small");
        $("#main-title").removeClass();
        $("#main-title h1").removeClass();
        $("#main-title").addClass("main-title-small");
        $(".continue-text").hide();
        $(".start-button").show();
        $(".start-button").addClass("animated flipInX animated-delay-1");
        openingPage = false;
    }
});

$(window).click(function() {
    if (openingPage) {
        $("#main-logo").removeClass();
        $("#main-logo").addClass("main-logo-small");
        $("#main-title").removeClass();
        $("#main-title h1").removeClass();
        $("#main-title").addClass("main-title-small");
        $(".continue-text").hide();
        $(".start-button").show();
        $(".start-button").addClass("animated flipInX animated-delay-1");
        openingPage = false;
    }
});

$("#login-start-button").click(function() {
    $("#openingPage").removeClass();
    $("#opening-page").addClass("animated slideOutLeft");
    $("#login-page").removeClass();
    $("#login-page").show();
    $("#login-page").addClass("animated slideInRight");
    $("#login-back-button").removeClass();
    $("#login-back-button").show();
    $("#login-back-button").addClass("btn btn-default btn-block btn-primary back-button animated fadeIn");
    $("#create-account-back-button").hide();
});

$("#login-back-button").click(function() {
    $("#opening-page").removeClass();
    $("#opening-page").show();
    $("#opening-page").addClass("animated slideInLeft");
    $("#login-page").removeClass();
    $("#login-page").addClass("animated slideOutRight");
    $("#login-back-button").removeClass();
    $("#login-back-button").addClass("btn btn-default btn-block btn-primary back-button animated fadeOut");
});

$("#create-account-start-button").click(function() {
    $("#openingPage").removeClass();
    $("#opening-page").addClass("animated slideOutLeft");
    $("#create-account-page").removeClass();
    $("#create-account-page").show();
    $("#create-account-page").addClass("animated slideInRight");
    $("#create-account-back-button").removeClass();
    $("#create-account-back-button").show();
    $("#create-account-back-button").addClass("btn btn-default btn-block btn-primary back-button animated fadeIn");
    $("#login-back-button").hide();
});

$("#create-account-back-button").click(function() {
    $("#opening-page").removeClass();
    $("#opening-page").show();
    $("#opening-page").addClass("animated slideInLeft");
    $("#create-account-page").removeClass();
    $("#create-account-page").addClass("animated slideOutRight");
    $("#create-account-back-button").removeClass();
    $("#create-account-back-button").addClass("btn btn-default btn-block btn-primary back-button animated fadeOut");
});

$(".login-form-element").click(function() {
    $(this).select();
});