$(function() {  
    var twitter_url = "https://twitter.com/intent/tweet?";

    function popup(url){
    	var width  = 575,
            height = 400,
	    left   = ($(window).width()  - width)  / 2,
	    top    = ($(window).height() - height) / 2,
	    opts   = 'status=1' +
		     ',width='  + width  +
		     ',height=' + height +
		     ',top='    + top    +
	             ',left='   + left;
					        
	 window.open(url, 'twitter', opts);

    }

    $('.twitter-share').click(function(){
	url = twitter_url;
	el = $(this);

	original_ref = el.data('twitter-original-referer');
	if (typeof(original_ref) !== 'undefined') {
	   url += "original_referer=" + encodeURIComponent(original_ref) +"&";
	}

	related = el.data('twitter-related');
	if (typeof(related) !== 'undefined') {
	   url += "related=" + encodeURIComponent(related) +"&";
	}
	
	via = el.data('twitter-via');
	if (typeof(via) !== 'undefined') {
	   url += "via=" + encodeURIComponent(via) +"&";
	}

	text= el.data('twitter-text');
	
	if (typeof(text) !== 'undefined') {
	   url += "text=" + encodeURIComponent(text) +"&";
	}

	shared_url= el.data('twitter-url');

    	if (typeof(shared_url) !== 'undefined') {
	   url += "url=" + encodeURIComponent(shared_url) +"&";
	}
	popup(url);
	return false;
    })
	// Handler for .ready() called.
});
