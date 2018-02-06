$(function(){
   $(".level-select-img").css("height", $(".level-select-img").width() / 2);
   var level1Progress = $("meta").attr("data-level1-progress");
   var level2Progress = $("meta").attr("data-level2-progress");
   var level3Progress = $("meta").attr("data-level3-progress");
   var level4Progress = $("meta").attr("data-level4-progress");
   for (var i = 1; i <= level1Progress; i++) {
       $(".level-1-" + i).addClass("active");
   }
   for (var i = 1; i <= level2Progress; i++) {
       $(".level-2-" + i).addClass("active");
   }
   for (var i = 1; i <= level3Progress; i++) {
       $(".level-3-" + i).addClass("active");
   }
   for (var i = 1; i <= level4Progress; i++) {
       $(".level-4-" + i).addClass("active");
   }
});