(function () {
  var previews = document.querySelectorAll("[data-speakerdeck-url]");

  previews.forEach(function (preview) {
    var deckUrl = preview.getAttribute("data-speakerdeck-url");
    var directThumbnail = preview.getAttribute("data-speakerdeck-thumbnail");

    if (directThumbnail) {
      preview.addEventListener("error", function () {
        preview.src = preview.getAttribute("data-fallback-src");
      }, { once: true });
      preview.src = directThumbnail;
      return;
    }

    var endpoint = "https://speakerdeck.com/oembed.json?url=" + encodeURIComponent(deckUrl);

    fetch(endpoint)
      .then(function (response) {
        if (!response.ok) {
          throw new Error("Speaker Deck thumbnail request failed");
        }
        return response.json();
      })
      .then(function (data) {
        if (data.thumbnail_url) {
          preview.src = data.thumbnail_url;
        }
      })
      .catch(function () {
        // Keep the local preview image when Speaker Deck is unavailable.
      });
  });
}());
