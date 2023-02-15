<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
/**
 * jQuery Opacity Rollover plugin
 *
 * Copyright (c) 2009 Trent Foley (http://trentacular.com)
 * Licensed under the MIT License:
 *   http://www.opensource.org/licenses/mit-license.php
 */
;(function($) {
	var defaults = {
		mouseOutOpacity:   0.67,
		mouseOverOpacity:  1.0,
		fadeSpeed:         'fast',
		exemptionSelector: '.selected'
	};

	$.fn.opacityrollover = function(settings) {
		// Initialize the effect
=======
/**
 * jQuery Opacity Rollover plugin
 *
 * Copyright (c) 2009 Trent Foley (http://trentacular.com)
 * Licensed under the MIT License:
 *   http://www.opensource.org/licenses/mit-license.php
 */
;(function($) {
	var defaults = {
		mouseOutOpacity:   0.67,
		mouseOverOpacity:  1.0,
		fadeSpeed:         'fast',
		exemptionSelector: '.selected'
	};

	$.fn.opacityrollover = function(settings) {
		// Initialize the effect
>>>>>>> 994af625642c0b36d97cfdfb580e32c3df4b4e7c
=======
/**
 * jQuery Opacity Rollover plugin
 *
 * Copyright (c) 2009 Trent Foley (http://trentacular.com)
 * Licensed under the MIT License:
 *   http://www.opensource.org/licenses/mit-license.php
 */
;(function($) {
	var defaults = {
		mouseOutOpacity:   0.67,
		mouseOverOpacity:  1.0,
		fadeSpeed:         'fast',
		exemptionSelector: '.selected'
	};

	$.fn.opacityrollover = function(settings) {
		// Initialize the effect
>>>>>>> 994af625642c0b36d97cfdfb580e32c3df4b4e7c
=======
/**
 * jQuery Opacity Rollover plugin
 *
 * Copyright (c) 2009 Trent Foley (http://trentacular.com)
 * Licensed under the MIT License:
 *   http://www.opensource.org/licenses/mit-license.php
 */
;(function($) {
	var defaults = {
		mouseOutOpacity:   0.67,
		mouseOverOpacity:  1.0,
		fadeSpeed:         'fast',
		exemptionSelector: '.selected'
	};

	$.fn.opacityrollover = function(settings) {
		// Initialize the effect
>>>>>>> origin/master
		$.extend(this, defaults, settings);

		var config = this;

		function fadeTo(element, opacity) {
			var $target = $(element);
			
			if (config.exemptionSelector)
				$target = $target.not(config.exemptionSelector);	
			
			$target.fadeTo(config.fadeSpeed, opacity);
		}

		this.css('opacity', this.mouseOutOpacity)
			.hover(
				function () {
					fadeTo(this, config.mouseOverOpacity);
				},
				function () {
					fadeTo(this, config.mouseOutOpacity);
				});
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

		return this;
	};
})(jQuery);
=======

		return this;
	};
})(jQuery);
>>>>>>> 994af625642c0b36d97cfdfb580e32c3df4b4e7c
=======

		return this;
	};
})(jQuery);
>>>>>>> 994af625642c0b36d97cfdfb580e32c3df4b4e7c
=======

		return this;
	};
})(jQuery);
>>>>>>> origin/master
