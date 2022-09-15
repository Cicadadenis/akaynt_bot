jQuery(document).ready(function(){


	function topslider() {
		var wh = jQuery(window).height();
		var dh = jQuery(".center_block").innerHeight();
		var pt = wh/2-dh/2;
		jQuery('.content').css({'min-height':wh});
		if (pt>0){
			jQuery('.center_block').css({'padding-top':pt});
		}
	}
	topslider();
	jQuery(window).resize(function(){
		topslider();
	});
	
	jQuery.ripple("a.ripple_b", {
		debug:!1,
		on:"mouseenter",
		opacity:.4,
		color:"auto",
		multi:!0,
		duration:.6,
		easing:"linear"
	});


});