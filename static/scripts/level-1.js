$("navbar ul li").click(function() {
    $("navbar ul li").removeClass("active");
    $(this).addClass("active");
    $(".email-full h3").after($(".email-full h2"));
    $(".email").removeClass("email-full");
    $(".exit-button").hide();
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
   alert("This feature is only for B-Mail Prime. For now, please enjoy looking at your emails on our free platform. If you want to upgrade to B-Mail prime, simply email us at dev.team@bmail.com. Sorry for any inconvenience and thank you for choosing B-Mail.") 
});

$(function() {
   setTimeout(function() {
       $(".large-title").hide();
   }, 666);
});

$(".form-exit-button").click(function() {
    $(".start-form").hide();
});

$("#login").click(function() {
    $("#login-form").show();
});

$("#create-account").click(function() {
    $("#create-account-form").show();
});

$("#create-account-form").submit(function() {
    event.preventDefault();
    pwd = sha256($("#create-account-form input[name='password']").val());
    confPwd = sha256($("#create-account-form input[name='confirm-password']").val());
    account = $("#create-account-form input[name='account']").val();
    if (pwd === confPwd) {
        $("#create-account-submit input[name='account']").val(account);
        $("#create-account-submit input[name='password']").val(pwd);
        $("#create-account-submit").submit();
    } else {
        $("#create-account-form input[name='password']").val("");
        $("#create-account-form input[name='confirm-password']").val("");
    }
});

$("#login-form").submit(function() {
    event.preventDefault();
    pwd = sha256($("#login-form input[name='password']").val());
    account = $("#login-form input[name='account']").val();
    $("#login-submit input[name='account']").val(account);
    $("#login-submit input[name='password']").val(pwd);
    $("#login-submit").submit();
});