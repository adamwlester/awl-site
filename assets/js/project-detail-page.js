// assets/js/project-detail-page.js
// -----------------------------------------
// Behavior for project detail pages:
// 1) Image viewer carousel (arrows + thumbs)
// 2) Move .content-group-secondary into aside column
// -----------------------------------------

(function () {
  // ---------------------------------------
  // 1. IMAGE VIEWER BEHAVIOR
  //    - Centered active slide with peeking neighbors
  //    - Smaller, dimmer neighbors
  //    - Arrows hidden at ends
  //    - Scroll, arrows, and thumbs all stay in sync
  // ---------------------------------------
  var viewer = document.querySelector('[data-image-viewer]');
  if (!viewer) return;

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

  function scrollToSlide(index, behavior) {
    var slide = slides[index];
    if (!slide || !slide.scrollIntoView) return;

    try {
      slide.scrollIntoView({
        behavior: behavior || 'smooth',
        block: 'nearest',
        inline: 'center'
      });
    } catch (e) {
      // Older browsers may not support options; fall back to default.
      slide.scrollIntoView();
    }
  }

  function updateSlideActiveClasses() {
    slides.forEach(function (slide, i) {
      if (i === activeIndex) {
        slide.classList.add('image-slide--active');
      } else {
        slide.classList.remove('image-slide--active');
      }
    });
  }

  function updateThumbs() {
    if (!thumbs.length) return;

    thumbs.forEach(function (thumb, i) {
      if (i === activeIndex) {
        thumb.classList.add('image-viewer-thumb--active');
      } else {
        thumb.classList.remove('image-viewer-thumb--active');
      }
    });
  }

  function updateArrows() {
    var lastIndex = slides.length - 1;

    if (prevButton) {
      if (activeIndex <= 0) {
        prevButton.classList.add('image-viewer-arrow--hidden');
        prevButton.setAttribute('aria-hidden', 'true');
        prevButton.setAttribute('aria-disabled', 'true');
        prevButton.setAttribute('tabindex', '-1');
      } else {
        prevButton.classList.remove('image-viewer-arrow--hidden');
        prevButton.removeAttribute('aria-hidden');
        prevButton.removeAttribute('aria-disabled');
        prevButton.removeAttribute('tabindex');
      }
    }

    if (nextButton) {
      if (activeIndex >= lastIndex) {
        nextButton.classList.add('image-viewer-arrow--hidden');
        nextButton.setAttribute('aria-hidden', 'true');
        nextButton.setAttribute('aria-disabled', 'true');
        nextButton.setAttribute('tabindex', '-1');
      } else {
        nextButton.classList.remove('image-viewer-arrow--hidden');
        nextButton.removeAttribute('aria-hidden');
        nextButton.removeAttribute('aria-disabled');
        nextButton.removeAttribute('tabindex');
      }
    }
  }

  /**
   * Set the active slide by index.
   *
   * options:
   *   - behavior: 'smooth' | 'auto'
   *   - fromScroll: true to avoid re-scrolling during scroll settling
   *   - force: true to reapply state even if index hasn't changed
   */
  function setActive(index, options) {
    index = clampIndex(index);

    var fromScroll = options && options.fromScroll;
    var behavior = (options && options.behavior) || 'smooth';
    var force = options && options.force;

    if (!force && index === activeIndex) {
      // Still make sure arrows/thumbs/classes are in a good state when used defensively.
      updateSlideActiveClasses();
      updateThumbs();
      updateArrows();
      return;
    }

    activeIndex = index;

    updateSlideActiveClasses();
    updateThumbs();
    updateArrows();

    if (!fromScroll) {
      scrollToSlide(activeIndex, behavior);
    }
  }

  function handleArrow(delta) {
    setActive(activeIndex + delta, { behavior: 'smooth' });
  }

  // Arrow click handlers
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

  // Thumbnail click handlers
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

  // Scroll-driven activation: when scrolling settles, pick the slide
  // whose center is closest to the center of the track.
  var scrollTimeoutId = null;

  track.addEventListener('scroll', function () {
    if (scrollTimeoutId !== null) {
      window.clearTimeout(scrollTimeoutId);
    }

    scrollTimeoutId = window.setTimeout(function () {
      scrollTimeoutId = null;

      var trackRect = track.getBoundingClientRect();
      var trackCenterX = trackRect.left + trackRect.width / 2;

      var nearestIndex = activeIndex;
      var nearestDistance = Infinity;

      slides.forEach(function (slide, index) {
        var slideRect = slide.getBoundingClientRect();
        var slideCenterX = slideRect.left + slideRect.width / 2;
        var distance = Math.abs(slideCenterX - trackCenterX);

        if (distance < nearestDistance) {
          nearestDistance = distance;
          nearestIndex = index;
        }
      });

      setActive(nearestIndex, { behavior: 'auto', fromScroll: true });
    }, 80);
  });

  // Initialize state so the first slide is centered and lifted.
  setActive(0, { behavior: 'auto', force: true });
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

(function () {
  // ---------------------------------------
  // 3. 3D MODEL VIEWER CONTROLS
  //    - Fullscreen toggle on the panel
  //    - Reset camera to initial on-load view
  // ---------------------------------------
  var panels = Array.prototype.slice.call(
    document.querySelectorAll('.model-viewer-panel')
  );
  if (!panels.length) return;

  // Helper: feature-detect fullscreen
  function isPanelFullscreen(panel) {
    return (
      document.fullscreenElement === panel ||
      document.webkitFullscreenElement === panel ||
      document.mozFullScreenElement === panel ||
      document.msFullscreenElement === panel
    );
  }

  function requestPanelFullscreen(panel) {
    if (panel.requestFullscreen) {
      panel.requestFullscreen();
    } else if (panel.webkitRequestFullscreen) {
      panel.webkitRequestFullscreen();
    } else if (panel.mozRequestFullScreen) {
      panel.mozRequestFullScreen();
    } else if (panel.msRequestFullscreen) {
      panel.msRequestFullscreen();
    }
  }

  function exitFullscreen() {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
    } else if (document.mozCancelFullScreen) {
      document.mozCancelFullScreen();
    } else if (document.msExitFullscreen) {
      document.msExitFullscreen();
    }
  }

  panels.forEach(function (panel) {
    var model = panel.querySelector('model-viewer');
    if (!model) return;

    var fullscreenButton = panel.querySelector('[data-model-viewer-fullscreen]');
    var resetButton = panel.querySelector('[data-model-viewer-reset]');

    if (!fullscreenButton && !resetButton) return;

    // -----------------------------
    // Capture initial camera state
    // -----------------------------
    var initialCameraState = null;

    function captureInitialCameraState() {
      if (initialCameraState) return;

      var orbitString = null;
      var targetString = null;
      var fovString = null;

      // Prefer JS properties (include defaults), fall back to attributes.
      try {
        if (model.cameraOrbit && typeof model.cameraOrbit.toString === 'function') {
          orbitString = model.cameraOrbit.toString();
        }
      } catch (e) {
        // Ignore, fall back to attribute.
      }
      if (!orbitString) {
        orbitString = model.getAttribute('camera-orbit');
      }

      try {
        if (model.cameraTarget && typeof model.cameraTarget.toString === 'function') {
          targetString = model.cameraTarget.toString();
        }
      } catch (e2) {
        // Ignore, fall back to attribute.
      }
      if (!targetString) {
        targetString = model.getAttribute('camera-target');
      }

      try {
        if (model.fieldOfView && typeof model.fieldOfView.toString === 'function') {
          fovString = model.fieldOfView.toString();
        }
      } catch (e3) {
        // Ignore, fall back to attribute.
      }
      if (!fovString) {
        fovString = model.getAttribute('field-of-view');
      }

      initialCameraState = {
        orbit: orbitString,
        target: targetString,
        fov: fovString
      };
    }

    // Capture as early as possible and again on load to pick up defaults.
    captureInitialCameraState();
    model.addEventListener('load', function handleModelLoad() {
      captureInitialCameraState();
      model.removeEventListener('load', handleModelLoad);
    });

    // -----------------------------
    // Reset button behavior
    // -----------------------------
    function resetCameraToInitial() {
      if (!initialCameraState) {
        captureInitialCameraState();
      }
      if (!initialCameraState) return;

      var state = initialCameraState;

      // Reset orbit
      if (state.orbit) {
        try {
          model.cameraOrbit = state.orbit;
        } catch (e) {
          model.setAttribute('camera-orbit', state.orbit);
        }
      } else {
        model.removeAttribute('camera-orbit');
      }

      // Reset target
      if (state.target) {
        try {
          model.cameraTarget = state.target;
        } catch (e2) {
          model.setAttribute('camera-target', state.target);
        }
      } else {
        model.removeAttribute('camera-target');
      }

      // Reset field of view (zoom)
      if (state.fov) {
        try {
          model.fieldOfView = state.fov;
        } catch (e3) {
          model.setAttribute('field-of-view', state.fov);
        }
      } else {
        model.removeAttribute('field-of-view');
      }
    }

    if (resetButton) {
      resetButton.addEventListener('click', function (event) {
        event.preventDefault();
        resetCameraToInitial();
        // Remove focus ring after activation
        resetButton.blur();
      });
    }

    // -----------------------------
    // Fullscreen button behavior
    // -----------------------------
    function updateFullscreenButtonState() {
      if (!fullscreenButton) return;

      var active = isPanelFullscreen(panel);
      fullscreenButton.setAttribute(
        'aria-label',
        active ? 'Exit fullscreen' : 'Enter fullscreen'
      );

      if (active) {
        fullscreenButton.classList.add('model-viewer-button--active');
      } else {
        fullscreenButton.classList.remove('model-viewer-button--active');
      }
    }

    if (fullscreenButton) {
      fullscreenButton.addEventListener('click', function (event) {
        event.preventDefault();

        if (isPanelFullscreen(panel) || document.fullscreenElement) {
          exitFullscreen();
        } else {
          requestPanelFullscreen(panel);
        }

        fullscreenButton.blur();
      });

      // React to user-initiated or ESC-based exits.
      document.addEventListener('fullscreenchange', updateFullscreenButtonState);
      document.addEventListener('webkitfullscreenchange', updateFullscreenButtonState);
      document.addEventListener('mozfullscreenchange', updateFullscreenButtonState);
      document.addEventListener('MSFullscreenChange', updateFullscreenButtonState);

      // Initialize button state.
      updateFullscreenButtonState();
    }
  });
})();

