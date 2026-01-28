// Smooth scrolling
$(function() {
  $('a[href*="#"]:not([href="#"])').click(function() {
    var hash = this.hash;

    // Close mobile navbar when clicking anchor links
    if ($('.navbar-collapse').hasClass('in')) {
      $('.navbar-collapse').removeClass('in').attr('aria-expanded', 'false');
      $('.navbar-toggle').attr('aria-expanded', 'false');
    }

    if (this instanceof SVGAElement){
      var target = $(this.href.baseVal);
      target = target.length ? target : $('[name=' + hash.slice(1) +']');
      if (target.length) {
        target_top = target.offset().top
        $('html, body').animate({
          scrollTop: target_top
        }, 1000, function() {
          history.pushState(null, null, hash);
        });
        return false;
      }
    }
    else if ((location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname)) {
      var target = $(hash);
      target = target.length ? target : $('[name=' + hash.slice(1) +']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top - 50
        }, 1000, function() {
          history.pushState(null, null, hash);
        });
        return false;
      }
    }
  });
});
