
(function ($) {
  'use strict';

  // Preloader js    
  $(window).on('load', function () {
    $('.preloader').fadeOut(100);
  });

  // Sticky Menu
  $(window).scroll(function () {
    if ($('.navigation').offset().top > 100) {
      $('.navigation').addClass('nav-bg');
    } else {
      $('.navigation').removeClass('nav-bg');
    }
  });

  // Background-images
  $('[data-background]').each(function () {
    $(this).css({
      'background-image': 'url(' + $(this).data('background') + ')'
    });
  });

  // venobox popup 
  $('.venobox').venobox();

  // dropdown menu
  var mobileWidth = 992;
  var navcollapse = $('.navbar .dropdown');
  $(window).on('resize', function () {
    navcollapse.children('.dropdown-menu').hide();
  });
  navcollapse.hover(function () {
    if ($(window).innerWidth() >= mobileWidth) {
      $(this).children('.dropdown-menu').stop(true, false, true).slideToggle(250);
    }
  });

  // Progress Bar
  $(window).on('load', function () {
    $('.progress-bar').each(function () {
      var width = $(this).data('percent');
      $(this).css({
        'transition': 'width 3s'
      });
      $(this).appear(function () {
        $(this).css('width', width + '%');
        $(this).find('.count').countTo({
          from: 0,
          to: width,
          speed: 3000,
          refreshInterval: 50
        });
      });
    });
  });

  // Shuffle js filter and masonry
  var containerEl = document.querySelector('.shuffle-wrapper');
  if (containerEl) {
    var Shuffle = window.Shuffle;
    var myShuffle = new Shuffle(document.querySelector('.shuffle-wrapper'), {
      itemSelector: '.shuffle-item',
      buffer: 1
    });

    jQuery('input[name="shuffle-filter"]').on('change', function (evt) {
      var input = evt.currentTarget;
      if (input.checked) {
        myShuffle.filter(input.value);
      }
    });
  }

  // video iframe load
  $('.play-icon i').on('click', function () {
    var video = '<iframe allowfullscreen src="' + $(this).attr('data-video') + '"></iframe>';
    $(this).replaceWith(video);
  });

  // Accordions
  $('.collapse').on('shown.bs.collapse', function () {
    $(this).parent().find('.ti-plus').removeClass('ti-plus').addClass('ti-minus');
  }).on('hidden.bs.collapse', function () {
    $(this).parent().find('.ti-minus').removeClass('ti-minus').addClass('ti-plus');
  });

  // clients logo slider
  $('.client-logo-slider').slick({
    infinite: true,
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: true,
    dots: false,
    arrows: false,
    responsive: [{
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 400,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  });

  // testimonial slider
  var containerEl2 = document.querySelector('#slider');
  if (containerEl2) {
    window.slider = $('#slider').cardSlider({
      slideClass: 'slide',
      delay: 300,
      transition: 'ease'
    });
  }

  $( ".sidebar .main-link" ).each(function() {
    var href = $(this).attr('href');
    var currentURL = window.location.pathname;
    if (href === currentURL) {
      $(this).addClass('active')
      $(this).parent().find('.main-sub-link').addClass('active')
      $(this).parent().find('i').addClass('active')
    }
    if ($(this).parent().find('.main-sub-link').length == 0) {
      $(this).parent().find('i').css({"visibility": "hidden"});
    }
  });
  
  $('.sidebar i.icon-xs.ti-angle-down').on('click', function () {
    if ($(this).hasClass('active') === true) {
      $(this).removeClass('active')
      $(this).parent().find('.main-link').removeClass('active')
      $(this).parent().find('.main-sub-link').removeClass('active')
    }
    else {
      $(this).addClass('active')
      $(this).parent().find('.main-link').addClass('active')
      $(this).parent().find('.main-sub-link').addClass('active')
    }
  });

  $( ".sidebar .sublink" ).each(function() {
    var subHref = $(this).attr('href');
    var subCurrentURL = window.location.pathname;
    if (subHref === subCurrentURL) {
      $(this).parent().parent().find('.main-sub-link').addClass('active')
      $(this).parent().parent().find('.main-link').addClass('active')
      $(this).parent().parent().find('i').addClass('active')
    }
  });

  $('.highlight pre code')
  .parent()
  .append('<div class="bode-btn-group btn-group btn-group-sm" role="group" aria-label="..."><button class="btn btn-dark copy-code" style=""><i class="icon-xs text-white ti-clipboard"></i></button></div>');
  $( ".highlight pre code" ).addClass( "code-block" )
  
})(jQuery);

// TableOfContents JS
class TableOfContents {
  /*
      The parameters from and to must be Element objects in the DOM.
  */
  constructor({ from, to }) {
      this.fromElement = from;
      this.toElement = to;
      // Get all the ordered headings.
      this.headingElements = this.fromElement.querySelectorAll("h2, h3");
      this.tocElement = document.createElement("div");
  }

  /*
      Get the most important heading level.
      For example if the article has only <h2>, <h3> and <h4> tags
      this method will return 2.
  */
  getMostImportantHeadingLevel() {
      let mostImportantHeadingLevel = 6; // <h6> heading level
      for (let i = 0; i < this.headingElements.length; i++) {
          let headingLevel = TableOfContents.getHeadingLevel(this.headingElements[i]);
          mostImportantHeadingLevel = (headingLevel < mostImportantHeadingLevel) ?
              headingLevel : mostImportantHeadingLevel;
      }
      return mostImportantHeadingLevel;
  }

  /*
      Generate a unique id string for the heading from its text content.
  */
  static generateId(headingElement) {
      return headingElement.textContent.replace(/\s+/g, "_");
  }

  /*
      Convert <h1> to 1 … <h6> to 6.
  */
  static getHeadingLevel(headingElement) {
      switch (headingElement.tagName.toLowerCase()) {
          case "h1": return 1;
          case "h2": return 2;
          case "h3": return 3;
          case "h4": return 4;
          case "h5": return 5;
          case "h6": return 6;
          default: return 1;
      }
  }

  generateToc() {
      let currentLevel = this.getMostImportantHeadingLevel() - 1,
          currentElement = this.tocElement;

      for (let i = 0; i < this.headingElements.length; i++) {
          let headingElement = this.headingElements[i],
              headingLevel = TableOfContents.getHeadingLevel(headingElement),
              headingLevelDifference = headingLevel - currentLevel,
              linkElement = document.createElement("a");
          
         

          if (!headingElement.id) {
              headingElement.id = TableOfContents.generateId(headingElement);
          }
          linkElement.href = `#${headingElement.id}`;
          linkElement.textContent = headingElement.textContent;
          linkElement.classList.add('nav-link')

          if (headingLevelDifference > 0) {
              // Go down the DOM by adding list elements.
              for (let j = 0; j < headingLevelDifference; j++) {
                  let listElement = document.createElement("ul"),
                      listItemElement = document.createElement("li");
                  listElement.appendChild(listItemElement);
                  currentElement.appendChild(listElement);
                  currentElement = listItemElement;
              }
              currentElement.appendChild(linkElement);
          } else {
              // Go up the DOM.
              for (let j = 0; j < -headingLevelDifference; j++) {
                  currentElement = currentElement.parentNode.parentNode;
              }
              let listItemElement = document.createElement("li");
              listItemElement.appendChild(linkElement);
              currentElement.parentNode.appendChild(listItemElement);
              currentElement = listItemElement;
          }

          currentLevel = headingLevel;
      }

      this.toElement.appendChild(this.tocElement.firstChild);
  }
}

document.addEventListener("DOMContentLoaded", () =>
  new TableOfContents({
      from: document.querySelector(".content-section"),
      to: document.querySelector(".table-of-contents")
  }).generateToc()
);