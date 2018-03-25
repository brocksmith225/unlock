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