var index = 1;

setTimeout(function() {
    nextBackground();
}, 30000);

function nextBackground() {
    $("body").css("background-image", "url(/static/img/pursue/pursue-" + (index+1) + ".JPG)");
    index = (index+1) % 3;
    setTimeout(function() {
        nextBackground();
    }, 30000);
}

$(function() {
    var target = $("#offerings .container");
    $("#offerings-background").css({top:target.position().top, left:"calc(50vw - " + (target.outerWidth()/2+15) + "px)", width:target.outerWidth(), height:target.outerHeight()});
});

$("#pursue-create-account-form").submit(function(event) {
    event.preventDefault();
    var acc = $("#pursue-create-account-form input[name='account']").val();
    var pwd = $("#pursue-create-account-form input[name='password']").val();
    var confPwd = $("#pursue-create-account-form input[name='confirm-password']").val();
    if (pwd == confPwd) {
        $("#pursue-create-account-form-submit input[name='account']").val(acc);
        $("#pursue-create-account-form-submit input[name='password']").val(pwd);
        $("#pursue-create-account-form-submit").submit();
    } else {
        $("#pursue-create-account-form input[name='password']").val("");
        $("#pursue-create-account-form input[name='confirm-password']").val("");
    }
});

$(".account-actions-change").each(function() {
    if ($(this).html().includes("+")) {
        $(this).addClass("positive");
    } else if ($(this).html().includes("-")) {
        $(this).addClass("negative");
    }
});