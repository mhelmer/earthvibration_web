$( document ).ready(function() {
	
	var width = 4;
	var inc = 4;

	var $widget = $(".gallery-widget");
	var img = ".img-wrapper";

	$(".gallery-widget .browse" ).on( "click", function() {
		return false;
	});

	$widget.each(function(){
		$images = $( this ).children( img );
		$images.slice(width).hide();

		n = $images.length;
		
		$( this ).data("state", { first: 0, last: width-1, n: n });
	
	});

	$widget.children( " .right " ).on( "click", function() {
		var state = $( this ).parent().data( "state" );
		if (state.last < state.n - 1) {
			state.first += inc;
			state.last += inc;
		} else { return; }
		
		$img = $( this ).siblings( img );
		$img.slice(state.first - inc, state.first).hide();
		$img.slice(state.last - inc + 1, state.last + 1).show();
		$( this ).parent().data("state", state);
	});

$widget.children( " .left " ).on( "click", function() {
		var state = $( this ).parent().data( "state" );
		if (state.first >= inc) {
			state.first -= inc;
			state.last -= inc;
		} else { return; }

		$img = $( this ).siblings( img );
		$img.slice(state.first, state.first + inc).show();
		$img.slice(state.last + 1, state.last+ inc + 1).hide();
		$( this ).parent().data("state", state);
	});
});

$(function() {
    var image = $('.gallery-widget img');
    var box = $('.focus');
    var close = $('.focus .close');
    var images = $('.gallery-widget img ');
    
	$(".gallery-widget .img-wrapper > a" ).on( "click", function() {
		return false;
	});

    image.on('click', function() {
        var $this = $(this);
        var src = $this.attr('data-full');
		var height = $this.attr('data-full-height');
		var width = $this.attr('data-full-width');
        box.find('img').remove();
        box.append('<img src=\"' + src + '\" />');
		box.height(height);
		box.css('margin-top', -height/2);
		box.width(width);
		box.css('margin-left', -width/2);
        box.fadeIn();
        images.addClass('darken');
        images.append('<div class="overlay">');
    });
    close.on('click', function() {
        box.css('display', 'none');
        images.removeClass('darken');
        $('.overlay').remove();
    });
});
