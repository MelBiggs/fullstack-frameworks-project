$(document).ready(function(){
    // Filter by Issue on Product Page Pagination
    var urlParams = new URLSearchParams(window.location.search);
    urlParams.delete("page");
    let keys = urlParams.keys();
    for(key of keys) { 
        $("input[type=checkbox][name="+key+"]").prop("checked",true);
        $('.pagination-class').each(function(i, button) {
            var href = $(button).attr("href");
            $(button).attr("href", `${href}&${key}=on`);
        });
    }
// Give class "selected" to All, Face & Body tabs of Products Page when chosen 
     if (window.location.href.indexOf("products/face") > -1) {
        $("#face_products_filter").addClass("selected");
        $("#all_products_filter").removeClass("selected");
     }
      if (window.location.href.indexOf("products/body") > -1) {
        $("#body_products_filter").addClass("selected");
        $("#all_products_filter").removeClass("selected");
     }
});


 
