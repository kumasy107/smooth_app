$(window).scroll(function() {
    $(".animate").each(function() {
      var position = $(this).offset().top;
      var scroll = $(window).scrollTop();
      var windowHeight = $(window).height();
      if (scroll > position - windowHeight + 500) {
        $(this).addClass("active");
      }
    });
  });