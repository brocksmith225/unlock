/* global $ */
/* global sha256 */

function loginSubmit() {
    event.preventDefault();
    var inputs = $("#login-form input");
    var values = {};
    inputs.each(function() {
        if (this.name == "password") {
            values[this.name] = sha256(this.value);
        } else {
            values[this.name] = this.value;
        }
    });
    console.log(values);
    $.ajax({
       url: "../python/login.py",
       type: "POST",
       dataType: "text",
       data: JSON.stringify(values),
       contentType: "application/json",
       success: login
    });
}

$("#create-account-form").submit(function() {
    event.preventDefault();
    pwd = sha256($("#create-account-form input[name='password']").val());
    confPwd = sha256($("#create-account-form input[name='confirm-password']").val());
    email = $("#create-account-form input[name='email']").val();
    if (pwd === confPwd) {
        $("#create-account-submit input[name='email']").val(email);
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
    email = $("#login-form input[name='email']").val();
    $("#login-submit input[name='email']").val(email);
    $("#login-submit input[name='password']").val(pwd);
    $("#login-submit").submit();
});