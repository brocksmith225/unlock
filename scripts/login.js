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

var mouseOver = false;

$(".ui-bottom").mouseover(function() {
    mouseOver = true;
    $(".ui-bottom").addClass("active");
});

$(".ui-bottom").mouseout(function() {
    mouseOver = false;
    if (!$(".flag-input").is(":focus")) {
        $(".ui-bottom").removeClass("active");
    }
});

$(".flag-input").focusout(function() {
    if (!mouseOver) {
        $(".ui-bottom").removeClass("active");
    }
});