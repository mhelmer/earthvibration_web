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
    var widget = '#main div.gallery-widget';
    var $widget = $(widget);
    var $box = $widget.find('div.focus');
    var $close = $widget.find('div.close');
    var $images = $widget.find(' img ');
    
	$(".gallery-widget .img-wrapper > a" ).on( "click", function() {
		return false;
	});

    $images.on('click', function() {
        var $this = $(this);
        var src = $this.attr('data-full');
		var height = $this.attr('data-full-height');
		var width = $this.attr('data-full-width');
		var $mybox = $this.parents(widget).children('div.focus').fadeIn();
        $mybox.find('img').remove();
        $mybox.append('<img src=\"' + src + '\" />');
		$mybox.height(height);
		$mybox.css('margin-top', -height/2);
		$mybox.width(width);
		$mybox.css('margin-left', -width/2);
		var next = $this.parents("div.img-wrapper").next("div.img-wrapper").find("img");
		$mybox.data('next', next)
        $mybox.fadeIn();

		$this.parents(widget).children('div.close').fadeIn();
        $images.addClass('darken');
		$(" body ").addClass('modal-open');
    });
	$box.on('click', function() {
		var next = $(this).data('next');
		if (next.length > 0) {
			next.click();
		} else {
			$close.click();
		}
	});
    $close.on('click', function() {
        $box.fadeOut();
        $close.fadeOut();
        $images.removeClass('darken');
		$(" body ").removeClass('modal-open');
    });
});
