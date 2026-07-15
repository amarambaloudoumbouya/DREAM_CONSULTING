(function ($) {
  "use strict";

  // Sticky Header Js

  var windowOn = $(window);

  windowOn.on("scroll", function () {
    var scroll = windowOn.scrollTop();
    if (scroll < 400) {
      $("#header-sticky").removeClass("header-sticky");
    } else {
      $("#header-sticky").addClass("header-sticky");
    }
  });

  //Header Search Form
  if ($(".search-trigger").length) {
    $(".search-trigger").on("click", function () {
      $("body").addClass("search-active");
    });
    $(".close-search, .search-back-drop").on("click", function () {
      $("body").removeClass("search-active");
    });
  }

  // Offcanvas menu
  $(".menu-trigger").on("click", function () {
    $(".extra-info,.offcanvas-overlay").addClass("active");
    return false;
  });
  $(".menu-close,.offcanvas-overlay").on("click", function () {
    $(".extra-info,.offcanvas-overlay").removeClass("active");
  });


  // data-backround

  $("[data-background").each(function () {
    $(this).css(
      "background-image",
      "url( " + $(this).attr("data-background") + "  )"
    );
  });

  // magnific popup

  $(".video-play-btn").magnificPopup({
    type: "iframe",
  });

  // Metis Menu

  $("#mobile-menu").metisMenu();

  $("#hamburger").on("click", function () {
    $(".mobile-nav").addClass("show");
    $(".overlay").addClass("active");
  });

  $(".close-nav").on("click", function () {
    $(".mobile-nav").removeClass("show");
    $(".overlay").removeClass("active");
  });

  $(".overlay").on("click", function () {
    $(".mobile-nav").removeClass("show");
    $(".overlay").removeClass("active");
  });

  // Hero Area Slider

  $(".homepage-slides").owlCarousel({
    items: 1,
    dots: false,
    nav: true,
    loop: true,
    autoplay: true,
    smartSpeed: 500,
    animateIn: "fadeIn",
    smartSpeed: 4000,    
    navText: [
      "<i class='las la-arrow-left'></i>",
      "<i class='las la-arrow-right'></i>",
    ],
    responsive: {
      0: {
        items: 1,
        nav: false,
        dots: false,
      },
      600: {
        items: 1,
        nav: false,
        dots: false,
      },
      768: {
        items: 1,
      },
      1100: {
        items: 1,
      },
    },
  });

  $(".homepage-slides").on("translate.owl.carousel", function () {
		$(".single-slide-item h1")
			.removeClass("animated fadeInDown")
			.css("opacity", "1");
		$(".single-slide-item h6")
			.removeClass("animated fadeInUp")
			.css("opacity", "1");
		$(".single-slide-item p")
			.removeClass("animated fadeInDown")
			.css("opacity", "1");
		$(".single-slide-item .white-btn")
			.removeClass("animated fadeInUp")
			.css("opacity", "1");
	});

	$(".homepage-slides").on("translated.owl.carousel", function () {
		$(".single-slide-item h1")
			.addClass("animated fadeInDown")
			.css("opacity", "1");
		$(".single-slide-item h6")
			.addClass("animated fadeInUp")
			.css("opacity", "1");
		$(".single-slide-item p")
			.addClass("animated fadeInDown")
			.css("opacity", "1");
		$(".single-slide-item .white-btn")
			.addClass("animated fadeInUp")
			.css("opacity", "1");
	});


  // Testimonial # 01

  $(".testimonial-one").owlCarousel({
    items: 1,
    dots: true,
    nav: false,
    loop: true,
    autoplay: false,
    autoplayTimeout: 5000,
    smartSpeed: 3000,
    slideSpeed: 300,
    margin: 30,
    navText: [
      "<i class='las la-arrow-left'></i>",
      "<i class='las la-arrow-right'></i>",
    ],
    
  });


    // Testimonial # 02

  $(".testimonial-two").owlCarousel({
    items: 1,
    dots: true,
    nav: false,
    loop: true,
    autoplay: false,
    autoplayTimeout: 5000,
    smartSpeed: 3000,
    slideSpeed: 300,
    margin: 50,
    navText: [
      "<i class='las la-arrow-left'></i>",
      "<i class='las la-arrow-right'></i>",
    ],
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,
        dots: true,
      },

      575: {
        items: 1,
        nav: false,
      },

      767: {
        items: 2,
        nav: false,
      },

      990: {
        items: 3,
        loop: true,
      },
      1200: {
        items: 3,
        loop: true,
      },
    },
  });

  // Project Slider

     $(".project-slider").owlCarousel({
    items: 1,
    margin: 30,
    dots: true,
    nav: true,
    loop: true,
    autoplay: true,
    responsiveClass: true,
    navText: [
      "<i class='las la-arrow-left'></i>",
      "<i class='las la-arrow-right'></i>",
    ],
    responsive: {
      575: {
        items: 1,
        nav: false,
        dots: false,
      },

      767: {
        items: 2,
        dots: true,
      },

      990: {
        items: 3,
        dots: false,
      },
      1200: {
        items: 3,
        dots: false,
      },
    },
  });


  $(".project-img-slider").owlCarousel({
      items: 3,
      dots: false,
      nav: false,
      loop: true,
      autoplay: true,
      autoplayTimeout: 5000,
      smartSpeed: 3000,
      slideSpeed: 300,
      navText: [
        "<i class='las la-arrow-left'></i>",
        "<i class='las la-arrow-right'></i>",
      ],
      responsiveClass: true,
      responsive: {
      0: {
        items: 1,
        dots: true,
      },

      575: {
        items: 1,
        nav: false,
      },

      767: {
        items: 3,
        nav: false,
      },

      990: {
        items: 3,
        loop: true,
      },
      1200: {
        items: 3,
        loop: true,
      },
    },
    });

  $(".project-img-slider-two").owlCarousel({
      items: 1,
      dots: false,
      nav: false,
      loop: true,
      autoplay: true,
      autoplayTimeout: 5000,
      animateIn: "fadeIn",
      smartSpeed: 3000,
      slideSpeed: 300,
      navText: [
        "<i class='las la-arrow-left'></i>",
        "<i class='las la-arrow-right'></i>",
      ],
      
    });

  $(".service-slider").owlCarousel({
      items: 4,
      dots: false,
      nav: false,
      loop: true,
      autoplay: true,
      autoplayTimeout: 5000,
      animateIn: "fadeIn",
      smartSpeed: 3000,
      slideSpeed: 300,
      navText: [
        "<i class='las la-arrow-left'></i>",
        "<i class='las la-arrow-right'></i>",
      ],
      responsiveClass: true,
      responsive: {
      0: {
        items: 1,
        dots: true,
      },

      575: {
        items: 1,
        nav: false,
      },

      767: {
        items: 3,
        nav: false,
      },

      990: {
        items: 3,
        loop: true,
      },
      1200: {
        items: 4,
        loop: true,
      },
    },
      
    });


  $(".hero-slider-wrap").owlCarousel({
      items: 1,
      dots: false,
      nav: false,
      loop: true,
      autoplay: true,
      autoplayTimeout: 5000,
      smartSpeed: 3000,
      slideSpeed: 300,
      animateIn: "fadeIn",
      navText: [
        "<i class='las la-arrow-left'></i>",
        "<i class='las la-arrow-right'></i>",
      ],      
      
    });

  $(".partner-slider").owlCarousel({
      items: 5,
      margin: 40,
      dots: false,
      nav: false,
      loop: true,
      autoplay: true,
      autoplayTimeout: 2500,
      autoplayHoverPause: true,
      smartSpeed: 1200,
      slideTransition: "linear",
      responsiveClass: true,
      responsive: {
        0: { items: 2 },
        575: { items: 3 },
        767: { items: 4 },
        990: { items: 5 },
      },
    });

 
  // Progress Bar JS

  $("#bar1").barfiller({
    barColor: "#1B1464",
    duration: 5000,
  });

  $("#bar2").barfiller({
    barColor: "#1B1464",
    duration: 5000,
  });

  $("#bar3").barfiller({
    barColor: "#1B1464",
    duration: 5000,
  });
  
  $("#bar4").barfiller({
    barColor: "#1B1464",
    duration: 5000,
  });

  $("#bar5").barfiller({
    barColor: "#1B1464",
    duration: 5000,
  });

  $("#bar6").barfiller({
    barColor: "#1B1464",
    duration: 5000,
  });

  // Wow Animation
  new WOW().init();

  // Nice select
  $("select").niceSelect();

  // Pure Counter

	new PureCounter();
	new PureCounter({
		filesizing: true,
		selector: ".filesizecount",
		pulse: 2,
	});

  // Active Class

  $(".main-menu ul > li > ul li a").on("mouseover", function () {
    $(".main-menu ul > li > ul li a").removeClass("active");
    $(this).addClass("active");
  });

  // Odometer js

  $(".odometer").appear(function (e) {
    var odo = $(".odometer");
    odo.each(function () {
      var countNumber = $(this).attr("data-count");
      $(this).html(countNumber);
    });
  });


  // Masonry Filter

  $(window).on("load", function () {
    var e = $(".project-filter"),
      a = $("#menu-filter");
    e.isotope({
      filter: "*",
      layoutMode: "masonry",
      animationOptions: {
        duration: 750,
        easing: "linear",
      },
    }),
      a.find("a").on("click", function () {
        var o = $(this).attr("data-filter");
        return (
          a.find("a").removeClass("active"),
          $(this).addClass("active"),
          e.isotope({
            filter: o,
            animationOptions: {
              animationDuration: 750,
              easing: "linear",
              queue: !1,
            },
          }),
          !1
        );
      });
  });


  // Contact Form

  $("#contactForm").on("submit", function (e) {
    e.preventDefault();

    var $action = $(this).prop("action");
    var $data = $(this).serialize();
    var $this = $(this);

    $this.prevAll(".alert").remove();

    $.post(
      $action,
      $data,
      function (data) {
        if (data.response === "error") {
          $this.before(
            '<div class="alert alert-danger">' + data.message + "</div>"
          );
        }

        if (data.response === "success") {
          $this.before(
            '<div class="alert alert-success">' + data.message + "</div>"
          );
          $this.find("input, textarea").val("");
        }
      },
      "json"
    );
  });

  // Visible From Right Slowly Animation
		let visibleSlowlyRight = document.querySelectorAll(".visible-slowly-right");
		if ($(visibleSlowlyRight).length > 0) {
			let char_come = gsap.utils.toArray(visibleSlowlyRight);
			char_come.forEach((char_come) => {
				let split_char = new SplitText(char_come, {
					type: "chars, words",
					lineThreshold: 0.5,
				});
				const tl2 = gsap.timeline({
					scrollTrigger: {
						trigger: char_come,
						start: "top 90%",
						end: "bottom 60%",
						scrub: false,
						markers: false,
						toggleActions: "play none none none",
					},
				});
				tl2.from(split_char.chars, {
					duration: 0.8,
					x: 70,
					autoAlpha: 0,
					stagger: 0.03,
				});
			});
		}

  //Hide Loading Box (Preloader)
  function handlePreloader() {
    if ($("#loader").length) {
      $("#loader").delay(200).fadeOut(500);
    }
  }

  $(window).on("load", function () {
    handlePreloader();
  });

  // Mouse Custom Cursor
  function itCursor() {
    var myCursor = jQuery(".mouseCursor");
    if (myCursor.length) {
      if ($("body")) {
        const e = document.querySelector(".cursor-inner"),
          t = document.querySelector(".cursor-outer");
        let n,
          i = 0,
          o = !1;
        (window.onmousemove = function (s) {
          o ||
            (t.style.transform =
              "translate(" + s.clientX + "px, " + s.clientY + "px)"),
            (e.style.transform =
              "translate(" + s.clientX + "px, " + s.clientY + "px)"),
            (n = s.clientY),
            (i = s.clientX);
        }),
          $("body").on("mouseenter", "button, a, .cursor-pointer", function () {
            e.classList.add("cursor-hover"), t.classList.add("cursor-hover");
          }),
          $("body").on("mouseleave", "button, a, .cursor-pointer", function () {
            ($(this).is("a", "button") &&
              $(this).closest(".cursor-pointer").length) ||
              (e.classList.remove("cursor-hover"),
              t.classList.remove("cursor-hover"));
          }),
          (e.style.visibility = "visible"),
          (t.style.visibility = "visible");
      }
    }
  }
  itCursor();
})(window.jQuery);
