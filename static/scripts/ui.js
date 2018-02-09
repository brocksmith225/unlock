var mouseOver = false;
var hintActive = false;

$("#hint").hide();

$(".ui-bottom").mouseover(function() {
    mouseOver = true;
    $(".ui-bottom").addClass("active");
});

$(".ui-bottom").mouseout(function() {
    mouseOver = false;
    if (!$(".flag-input").is(":focus") && $(".flag-check").html() == "CHECK" && !hintActive) {
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
                        alert("Congrats!");
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
       $("#hint").show();
       hintActive = true;
   }
});