$(document).ready(function() {

    // first only show home content
    $(".tab-content").hide();
    $(".tab-content-home").show();

    // show selected tab content
    $("#tab-home").click(function() {
    $(".tab-content").hide();
    $(".tab-content-home").show();
    });
    $("#tab-lists").click(function() {
    $(".tab-content").hide();
    $(".tab-content-lists").show();
    });
    $("#tab-favourites").click(function() {
    $(".tab-content").hide();
    $(".tab-content-favourites").show();
    });
    $("#tab-recipes").click(function() {
    $(".tab-content").hide();
    $(".tab-content-recipes").show();
    });
    $("#tab-supermarkets").click(function() {
    $(".tab-content").hide();
    $(".tab-content-supermarkets").show();
    });

});