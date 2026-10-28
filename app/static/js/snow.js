(function () {
  var container = document.querySelector('.snow');
  if (!container) return;

  var isSmall = window.innerWidth < 640;
  var count = isSmall ? 28 : 55;
  var glyphs = ['❄', '❅', '❆'];

  for (var i = 0; i < count; i++) {
    var flake = document.createElement('span');
    flake.className = 'snowflake';
    flake.textContent = glyphs[Math.floor(Math.random() * glyphs.length)];

    var size = (Math.random() * 14 + 8).toFixed(1);
    var left = (Math.random() * 100).toFixed(2);
    var duration = (Math.random() * 10 + 9).toFixed(2);
    var delay = (-Math.random() * duration).toFixed(2);
    var drift = (Math.random() * 80 - 40).toFixed(0);
    var opacity = (Math.random() * 0.5 + 0.35).toFixed(2);

    flake.style.left = left + 'vw';
    flake.style.fontSize = size + 'px';
    flake.style.opacity = opacity;
    flake.style.animationDuration = duration + 's';
    flake.style.animationDelay = delay + 's';
    flake.style.setProperty('--drift', drift + 'px');

    container.appendChild(flake);
  }
})();
