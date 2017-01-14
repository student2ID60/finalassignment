$(document).ready(function() {

    // first only show home content
    $(".tab-content").hide();
    $(".tab-content-home").show();

    // show selected tab content
    $("#tab-home").click(function() {
        $(".tab-item").removeClass("active");
        $("#tab-home").addClass("active");
        $(".tab-content").hide();
        $(".tab-content-home").show();
    });
    $("#tab-lists").click(function() {
        $(".tab-item").removeClass("active");
        $("#tab-lists").addClass("active");
        $(".tab-content").hide();
        $(".tab-content-lists").show();
    });
    $("#tab-favourites").click(function() {
        $(".tab-item").removeClass("active");
        $("#tab-favourites").addClass("active");
        $(".tab-content").hide();
        $(".tab-content-favourites").show();
    });
    $("#tab-recipes").click(function() {
        $(".tab-item").removeClass("active");
        $("#tab-recipes").addClass("active");
        $(".tab-content").hide();
        $(".tab-content-recipes").show();
    });
    $("#tab-supermarkets").click(function() {
        $(".tab-item").removeClass("active");
        $("#tab-supermarkets").addClass("active");
        $(".tab-content").hide();
        $(".tab-content-supermarkets").show();
    });

});