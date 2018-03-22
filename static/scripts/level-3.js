var index = 1;

setTimeout(function() {
    nextBackground();
}, 30000);

function nextBackground() {
    console.log("test");
    $("body").css("background-image", "url(/static/img/pursue/pursue-" + (index+1) + ".JPG)");
    index = (index+1) % 3;
    setTimeout(function() {
        nextBackground();
    }, 30000);
}