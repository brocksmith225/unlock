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

function login() {
    
}