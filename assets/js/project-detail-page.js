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
  //    - Scroll, arrows, thumbs, and drag all stay in sync
  // ---------------------------------------
  var viewer = document.querySelector('[data-image-viewer]');
  if (!viewer) return;

  var track = viewer.querySelector('[data-image-viewer-track]');
  if (!track) return;

  // Only treat slides with a data-image-index as real slides.
  // Ghost spacers at the ends (.image-slide--ghost) do not get this attribute
  // and are therefore ignored by all viewer logic.
  var slides = Array.prototype.slice.call(
    track.querySelectorAll('.image-slide[data-image-index]')
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

  // Caption element and per-slide captions (derived from <img alt>)
  var captionEl = viewer.querySelector('[data-image-viewer-caption]');
  var captions = slides.map(function (slide) {
    var img = slide.querySelector('img');
    if (!img) return '';
    return img.getAttribute('alt') || '';
  });

  var activeIndex = 0;

  // Drag-to-scroll state (desktop)
  var isDragging = false;
  var dragStartX = 0;
  var dragStartScrollLeft = 0;
  var DRAG_MOVE_THRESHOLD = 4;

  function clampIndex(index) {
    if (index < 0) return 0;
    if (index >= slides.length) return slides.length - 1;
    return index;
  }

  // Center a slide using its offset inside the track.
  // This is more stable than rect math and guarantees that
  // the first and last slides can land perfectly centered.
  function scrollToSlide(index, behavior) {
    var slide = slides[index];
    if (!slide) return;

    // Position of the slide inside the scrollable track
    var slideLeft = slide.offsetLeft;
    var slideWidth = slide.offsetWidth;
    var trackWidth = track.clientWidth;

    // Ideal scrollLeft so the slide's center aligns with track center
    var targetScroll =
      slideLeft - (trackWidth - slideWidth) / 2;

    // Clamp into the valid scroll range
    var maxScroll = track.scrollWidth - trackWidth;
    if (maxScroll < 0) maxScroll = 0;

    if (targetScroll < 0) targetScroll = 0;
    if (targetScroll > maxScroll) targetScroll = maxScroll;

    var mode = behavior || 'smooth';

    if (!track.scrollTo || mode === 'auto') {
      track.scrollLeft = targetScroll;
    } else {
      track.scrollTo({
        left: targetScroll,
        behavior: mode
      });
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

  // Update the visible caption below the active image
  function updateCaption() {
    if (!captionEl) return;
    var text = captions[activeIndex] || '';
    captionEl.textContent = text;
  }

  /**
   * Set the active slide by index.
   *
   * options:
   *   - behavior: 'smooth' | 'auto'
   *   - force: true to reapply state even if index hasn't changed
   */
  function setActive(index, options) {
    index = clampIndex(index);

    var behavior = (options && options.behavior) || 'smooth';
    var force = options && options.force;

    if (!force && index === activeIndex) {
      // Keep state consistent when called defensively.
      updateSlideActiveClasses();
      updateThumbs();
      updateArrows();
      updateCaption();
      return;
    }

    activeIndex = index;

    updateSlideActiveClasses();
    updateThumbs();
    updateArrows();
    updateCaption();

    scrollToSlide(activeIndex, behavior);
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

  // Keyboard arrow key navigation:
  // Left arrow → previous slide, Right arrow → next slide.
  // Prevents the tiny native scroll "eek" and makes each key press
  // cleanly step between slides instead.
  window.addEventListener('keydown', function (event) {
    if (!slides.length) return;

    if (event.key === 'ArrowLeft') {
      handleArrow(-1);
      event.preventDefault();
    } else if (event.key === 'ArrowRight') {
      handleArrow(1);
      event.preventDefault();
    }
  });

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

  // Find the slide nearest to the visual center of the track.
  function snapToNearest() {
    if (!slides.length) return;

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

    setActive(nearestIndex, { behavior: 'smooth' });
  }

  // Desktop drag-to-scroll on the main track
  track.addEventListener('mousedown', function (event) {
    // Left button only
    if (event.button !== 0) return;

    isDragging = true;
    dragStartX = event.clientX;
    dragStartScrollLeft = track.scrollLeft;

    track.classList.add('image-viewer-track--dragging');
  });

  window.addEventListener('mousemove', function (event) {
    if (!isDragging) return;

    var deltaX = event.clientX - dragStartX;

    // Treat as a drag once we move a bit; prevent text selection.
    if (Math.abs(deltaX) >= DRAG_MOVE_THRESHOLD) {
      event.preventDefault();
    }

    track.scrollLeft = dragStartScrollLeft - deltaX;
  });

  function endDrag() {
    if (!isDragging) return;

    isDragging = false;
    track.classList.remove('image-viewer-track--dragging');

    // After a drag, snap once to the nearest slide.
    snapToNearest();
  }

  window.addEventListener('mouseup', endDrag);
  window.addEventListener('mouseleave', endDrag);

  // Scroll-driven activation (wheel / touch / keyboard):
  // when scrolling settles and we're not actively dragging,
  // snap the nearest slide into center.
  var scrollTimeoutId = null;

  track.addEventListener('scroll', function () {
    if (isDragging) {
      // During drag we let the strip move freely; snapping happens on mouseup.
      return;
    }

    if (scrollTimeoutId !== null) {
      window.clearTimeout(scrollTimeoutId);
    }

    scrollTimeoutId = window.setTimeout(function () {
      scrollTimeoutId = null;
      snapToNearest();
    }, 80);
  });

  // Initialize state so the first slide is centered and lifted.
  setActive(0, { behavior: 'auto', force: true });

  // ---------------------------------------
  // Ensure centering after images load and on resize
  // ---------------------------------------

  function recenterActiveSlide() {
    // Reapply current index with fresh geometry
    setActive(activeIndex, { behavior: 'auto', force: true });
  }

  // When images finish loading, recenter once.
  var viewerImages = Array.prototype.slice.call(
    track.querySelectorAll('img')
  );

  var pending = 0;
  viewerImages.forEach(function (img) {
    if (img.complete && img.naturalWidth !== 0) {
      return;
    }
    pending += 1;
    img.addEventListener(
      'load',
      function handleImgLoad() {
        pending -= 1;
        if (pending <= 0) {
          recenterActiveSlide();
        }
      },
      { once: true }
    );
  });

  // If all images were already loaded from cache,
  // still do one recenter pass.
  if (pending === 0) {
    recenterActiveSlide();
  }

  // Recenter on window resize as well to handle width changes.
  window.addEventListener('resize', function () {
    recenterActiveSlide();
  });
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

(function () {
  // ---------------------------------------
  // 4. IMAGE VIEWER FULLSCREEN TOGGLE
  //    - Fullscreen on the entire .image-viewer panel
  //    - Reuses the same visual affordance as the 3D viewer
  // ---------------------------------------
  var viewer = document.querySelector('[data-image-viewer]');
  if (!viewer) return;

  var fullscreenButton = viewer.querySelector('[data-image-viewer-fullscreen]');
  if (!fullscreenButton) return;

  // Helper: feature-detect fullscreen for a given panel
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

  function updateFullscreenButtonState() {
    var active = isPanelFullscreen(viewer);

    fullscreenButton.setAttribute(
      'aria-label',
      active ? 'Exit fullscreen' : 'Enter fullscreen'
    );

    if (active) {
      fullscreenButton.classList.add('image-viewer-button--active');
    } else {
      fullscreenButton.classList.remove('image-viewer-button--active');
    }
  }

  fullscreenButton.addEventListener('click', function (event) {
    event.preventDefault();

    if (isPanelFullscreen(viewer) || document.fullscreenElement) {
      exitFullscreen();
    } else {
      requestPanelFullscreen(viewer);
    }

    // Remove focus ring after activation
    fullscreenButton.blur();
  });

  // Keep button state in sync for user-initiated fullscreen changes
  document.addEventListener('fullscreenchange', updateFullscreenButtonState);
  document.addEventListener('webkitfullscreenchange', updateFullscreenButtonState);
  document.addEventListener('mozfullscreenchange', updateFullscreenButtonState);
  document.addEventListener('MSFullscreenChange', updateFullscreenButtonState);

  // Initialize state on load
  updateFullscreenButtonState();
})();
