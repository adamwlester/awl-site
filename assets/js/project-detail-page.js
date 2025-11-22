// assets/js/project-detail-page.js
// -----------------------------------------
// Behavior for project detail pages:
// 1) Image viewer carousel (arrows + thumbs)
// 2) Move .content-group-secondary into aside column
// -----------------------------------------

(function () {
  // ---------------------------------------
  // 1. IMAGE VIEWER BEHAVIOR
  // ---------------------------------------
  var viewer = document.querySelector('[data-image-viewer]');
  if (viewer) {
    var track = viewer.querySelector('[data-image-viewer-track]');
    if (!track) return;

    var slides = Array.prototype.slice.call(
      track.querySelectorAll('.image-slide')
    );
    if (!slides.length) return;

    var thumbsContainer = viewer.querySelector('[data-image-viewer-thumbnails]');
    var thumbs = thumbsContainer
      ? Array.prototype.slice.call(
          thumbsContainer.querySelectorAll('.image-viewer-thumb')
        )
      : [];

    var prevButton = viewer.querySelector('.image-viewer-arrow--prev');
    var nextButton = viewer.querySelector('.image-viewer-arrow--next');

    var activeIndex = 0;

    function clampIndex(index) {
      if (index < 0) return 0;
      if (index >= slides.length) return slides.length - 1;
      return index;
    }

    function setActive(index, options) {
      index = clampIndex(index);
      if (index === activeIndex) return;
      activeIndex = index;

      var slide = slides[activeIndex];
      if (slide && slide.scrollIntoView) {
        try {
          slide.scrollIntoView({
            behavior: (options && options.behavior) || 'smooth',
            block: 'nearest',
            inline: 'center'
          });
        } catch (e) {
          // Older browsers may not support options; fall back to default.
          slide.scrollIntoView();
        }
      }

      // Update active thumbnail state
      if (thumbs.length) {
        thumbs.forEach(function (thumb, i) {
          if (i === activeIndex) {
            thumb.classList.add('image-viewer-thumb--active');
          } else {
            thumb.classList.remove('image-viewer-thumb--active');
          }
        });
      }
    }

    function handleArrow(delta) {
      setActive(activeIndex + delta);
    }

    if (prevButton) {
      prevButton.addEventListener('click', function () {
        handleArrow(-1);
      });
    }

    if (nextButton) {
      nextButton.addEventListener('click', function () {
        handleArrow(1);
      });
    }

    if (thumbs.length) {
      thumbs.forEach(function (thumb) {
        thumb.addEventListener('click', function () {
          var indexAttr = thumb.getAttribute('data-image-index');
          var index = parseInt(indexAttr, 10);
          if (!isNaN(index)) {
            setActive(index, { behavior: 'smooth' });
          }
        });
      });
    }

    // Initialize state so the first thumbnail is synced with the first slide
    setActive(0, { behavior: 'auto' });
  }
})();

(function () {
  // ---------------------------------------
  // 2. MOVE SECONDARY CONTENT INTO ASIDE
  // ---------------------------------------
  var layout = document.querySelector('.project-layout');
  if (!layout) return;

  var mainColumn = layout.querySelector('.project-main-column');
  var asideColumn = layout.querySelector('.project-aside-column');
  if (!mainColumn || !asideColumn) return;

  // Find the secondary content group authored in the main column
  var secondary = mainColumn.querySelector('.content-group-secondary');
  if (!secondary) return;

  // Find the model viewer panel (if present) so secondary can sit below it
  var modelPanel = asideColumn.querySelector('.model-viewer-panel');

  // Detach from the main column
  if (secondary.parentNode) {
    secondary.parentNode.removeChild(secondary);
  }

  // Insert into the aside column:
  // - If a model panel exists, place secondary after it.
  // - Otherwise, append at the end of the aside column.
  if (modelPanel && modelPanel.parentNode === asideColumn) {
    if (modelPanel.nextSibling) {
      asideColumn.insertBefore(secondary, modelPanel.nextSibling);
    } else {
      asideColumn.appendChild(secondary);
    }
  } else {
    asideColumn.appendChild(secondary);
  }
})();
