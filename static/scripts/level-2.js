var cartItems = [];
var items = [];
var inCart = false;

$(function() {
    $("#items").children().each(function() {
        items.push(this);
    });
});

$("navbar i.fa-shopping-cart").click(function() {
    inCart = true;
    $("#items").html("");
    for (var i = 0; i < cartItems.length; i++) {
        $("#items").append(cartItems[i]);
    }
    $(".add-to-cart").click(function() {
        if (inCart) {
            $("#cart-counter").text(parseInt($("#cart-counter").text()) - 1);
            cartItems.splice($.inArray($(this).parent(), cartItems), 1);
            found = false;
            for (var i = 0; i < cartItems.length; i++) {
                console.log($(this).parent());
                console.log(cartItems[i]);
                console.log(cartItems[i].equals($(this).parent()));
                console.log(cartItems[i] == $(this).parent());
                if (cartItems[i].equals($(this).parent())) {
                    found = true;
                    i = cartItems.length;
                }
            }
            if (!found) {
                $(this).parent().remove();
            }
        } else {
            $("#cart-counter").text(parseInt($("#cart-counter").text()) + 1);
            cartItems.push($(this).parent());
        }
    });
});

$(".top-logo").click(function() {
    inCart = false;
    $("#items").html("");
    for (var i = 0; i < items.length; i++) {
        $("#items").append(items[i]);
    }
    $(".add-to-cart").click(function() {
        if (inCart) {
            $("#cart-counter").text(parseInt($("#cart-counter").text()) - 1);
            cartItems.splice($.inArray($(this).parent(), cartItems), 1);
            found = false;
            for (var i = 0; i < cartItems.length; i++) {
                if (cartItems[i] == $(this).parent()) {
                    found = true;
                    i = cartItems.length;
                }
            }
            if (!found) {
                $(this).parent().remove();
            }
        } else {
            $("#cart-counter").text(parseInt($("#cart-counter").text()) + 1);
            cartItems.push($(this).parent());
        }
    });
});

$(".add-to-cart").click(function() {
    if (inCart) {
        $("#cart-counter").text(parseInt($("#cart-counter").text()) - 1);
        cartItems.splice($.inArray($(this).parent(), cartItems), 1);
        found = false;
        for (var i = 0; i < cartItems.length; i++) {
            if (cartItems[i] == $(this).parent()) {
                found = true;
                i = cartItems.length;
            }
        }
        if (!found) {
            $(this).parent().remove();
        }
    } else {
        $("#cart-counter").text(parseInt($("#cart-counter").text()) + 1);
        cartItems.push($(this).parent());
    }
});

$("#search-button").click(function() {
    parent.updateLevelProgress(1);
    term = $("#search-input").val();
    if (term.indexOf("'") > -1 || term.indexOf(";") > -1 || term.indexOf("--") > -1) {
        parent.updateLevelProgress(2);
    }
    $.post({
        url: "/level-2/search",
        dataType: "text",
        data: $("#search-input").serialize(),
        success: function(result) {
            result = result.replace(/'/g, '"');
            searchItems = $.parseJSON(result);
            $("#items").html("");
            for (i = 0; i < searchItems.length; i++) {
                if (searchItems[i]["image"] == "letmein" || searchItems[i]["name"] == "letmein" || searchItems[i]["price"] == "letmein" ) {
                    parent.updateLevelProgress(3);
                }
                $("#items").append('<div class="item"><div class="preview-img" style="background-image: url(&quot;../static/img/nile/' + searchItems[i]["image"] + '&quot;);"></div><h1>' + searchItems[i]["name"] + '</h1><i class="fa fa-shopping-cart add-to-cart"></i><h2>' + searchItems[i]["price"] + '</h2></div>');
            }
        }
    });
});

$("#search-input").keypress(function(e) {
    if (e.which == 13) {
        parent.updateLevelProgress(1);
        term = $("#search-input").val();
        if (term.indexOf("'") > -1 || term.indexOf(";") > -1 || term.indexOf("--") > -1) {
            parent.updateLevelProgress(2);
        }
        $.post({
            url: "/level-2/search",
            dataType: "text",
            data: $("#search-input").serialize(),
            success: function(result) {
                result = result.replace(/'/g, '"');
                searchItems = $.parseJSON(result);
                $("#items").html("");
                for (i = 0; i < searchItems.length; i++) {
                    if (searchItems[i]["image"] == "letmein" || searchItems[i]["name"] == "letmein" || searchItems[i]["price"] == "letmein" ) {
                        parent.updateLevelProgress(3);
                    }
                    $("#items").append('<div class="item"><div class="preview-img" style="background-image: url(&quot;../static/img/nile/' + searchItems[i]["image"] + '&quot;);"></div><h1>' + searchItems[i]["name"] + '</h1><i class="fa fa-shopping-cart add-to-cart"></i><h2>' + searchItems[i]["price"] + '</h2></div>');
                }
            }
        });
    }
});

$("#search-input").click(function() {
    $(this).select();
});

$(function() {
    $(".nile-account-form").hide();
});

$("#sign-up").click(function() {
    $("#nile-sign-up").show();
    $("#nile-sign-in").hide();
    event.stopPropagation();
});

$("#sign-in").click(function() {
    $("#nile-sign-in").show();
    $("#nile-sign-up").hide();
    event.stopPropagation();
});

$(".nile-account-form").click(function() {
    event.stopPropagation();
});

$("body").click(function() {
    $(".nile-account-form").hide();
});

$(function() {
    if ($("meta").attr("data-username") == "realDonaldTrump") {
        parent.updateLevelProgress(4);
        alert("Congrats!");
        parent.redirect("info")
    }
})