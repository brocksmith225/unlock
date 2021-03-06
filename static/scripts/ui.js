var mouseOver = false;
var hintActive = false;

$("#hint").hide();

$(".ui-bottom").mouseover(function() {
    mouseOver = true;
    $(".ui-bottom").addClass("active");
});

$(".ui-bottom").mouseout(function() {
    mouseOver = false;
    if (!$(".flag-input").is(":focus") && !hintActive) {
        $(".ui-bottom").removeClass("active");
    }
});

$(".flag-input").focusout(function() {
    if (!mouseOver) {
        $(".ui-bottom").removeClass("active");
    }
});

$(".flag-input").focus(function() {
    $("#hint").hide();
    hintActive = false;
});

$(".flag-check").click(function() {
    if ($(this).html() == "CHECK") {
        $(this).html("<i class='fa fa-cog fa-spin'></i>");
        $.post({
    		url: "/flag-check/" + $("meta").attr("data-level"),
    		dataType: "text",
    		data: $(".flag-input").serialize(),
    		success: function(result) {
    		    $(".flag-check").html("CHECK");
                if (result == "true") {
                    alert("Congrats!");
                    window.location.replace("http://unlock.brockwsmith.com/level-" + $("meta").attr("data-level") + "/info");
                } else {
                    $(".flag-input").val("");
                    alert("Incorrect");
                }
    		}
    	});
    } else {
        $(this).html("CHECK");
        if (!mouseOver) {
            $(".ui-bottom").removeClass("active");
        }
    }
});

$(".flag-input").keypress(function(e) {
    if (e.which == 13) {
        if ($(".flag-check").html() == "CHECK") {
            $(".flag-check").html("<i class='fa fa-cog fa-spin'></i>");
            $.post({
        		url: "/flag-check/" + $("meta").attr("data-level"),
        		dataType: "text",
        		data: $(".flag-input").serialize(),
        		success: function(result) {
        		    $(".flag-check").html("CHECK");
                    if (result == "true") {
                        updateLevelProgress(3);
                        alert("Congrats!");
                        window.location.replace("https://unlock.brockwsmith.com/level-" + $("meta").attr("data-level") + "/info");
                    } else {
                        $(".flag-input").val("");
                        alert("Incorrect");
                    }
        		}
        	});
        } else {
            $(".flag-check").html("CHECK");
            if (!mouseOver) {
                $(".ui-bottom").removeClass("active");
            }
        }
    }
});

$("#hint-button").click(function() {
    if (hintActive) {
       $("#hint").hide();
       hintActive = false;
    } else {
       $.post({
    		url: "/get-hint/" + $("meta").attr("data-level"),
    		success: function(result) {
    		    $("#hint").text(result);
    		    $("#hint").show();
                hintActive = true;
    		}
        });
    }
});

updateLevelProgressDisplay();

function updateLevelProgressDisplay() {
    var levelProgress = $("meta").attr("data-level-progress");
    for (var i = 1; i <= levelProgress; i++) {
        $(".level-" + i).addClass("active");
    } 
}

function updateLevelProgress(progress) {
    if ($("meta").attr("data-level-progress") == progress-1) {
        $("meta").attr("data-level-progress", progress);
        updateLevelProgressDisplay();
    }
}

function redirect(url) {
    window.location.replace(url);
}

var myHistory;

$(function() {
    $("input[name='url']").val("https://unlock.brockwsmith.com/" + $("#page-loader").attr("src"));
    myHistory = new LinkedList("https://unlock.brockwsmith.com/" + $("#page-loader").attr("src"));
});

function updateURL(url) {
    if (myHistory.current.value == "") {
        myHistory.goTo(url);
    }
    $("input[name='url']").val(url);
}

notDone = true;

$("#page-loader").on("load", function() {
    if (notDone) {
        $("#back").click(function(e) {
            e.stopPropagation();
            var back = myHistory.back();
            $("input[name='url']").val(back);
            $("#page-loader").get(0).contentWindow.location.replace(back);
        });
        $("#forward").click(function() {
            e.stopPropagation();
            var forward = myHistory.forward();
            $("input[name='url']").val(forward);
            $("#page-loader").get(0).contentWindow.location.replace(forward);
        });
        notDone = false;
    }
});

$("input[name='url']").keypress(function(e) {
    e.stopPropagation();
    if (e.which == 13) {
        myHistory.goTo($("input[name='url']").val());
        $("#page-loader").get(0).contentWindow.location.replace($("input[name='url']").val());
    }
});

function LinkedList(url) {
    this.current = new Node(url);
    this.back = function() {
        if (this.current.hasBack()) {
            this.current = this.current.back;
            return this.current.value;
        } else {
            return this.current.value;
        }
    };
    this.forward = function() {
        if (this.current.hasForward()) {
            this.current = this.current.forward;
        }
        return this.current.value;
    };
    this.goTo = function(url) {
        this.current.forward = new Node(url);
        this.current.forward.back = this.current;
        this.current = this.current.forward;
    };
}

function Node(url) {
    this.value = url;
    this.back = null;
    this.forward = null;
    this.hasBack = function() {
        return this.back != null;
    };
    this.hasForward = function() {
        return this.forward != null;
    };
}
