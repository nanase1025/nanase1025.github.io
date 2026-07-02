(function () {
  function setLanguage(language) {
    var normalized = language === "ja" ? "ja" : "en";

    document.documentElement.setAttribute("data-language", normalized);
    document.documentElement.setAttribute("lang", normalized);

    try {
      window.localStorage.setItem("site-language", normalized);
    } catch (error) {
      // Ignore storage failures in private browsing or restricted contexts.
    }
  }

  function getSavedLanguage() {
    try {
      return window.localStorage.getItem("site-language") || "en";
    } catch (error) {
      return "en";
    }
  }

  setLanguage(getSavedLanguage());

  document.addEventListener("click", function (event) {
    var target = event.target;

    while (target && target !== document) {
      if (target.getAttribute && target.getAttribute("data-language-toggle") !== null) {
        event.preventDefault();

        var current = document.documentElement.getAttribute("data-language");
        setLanguage(current === "ja" ? "en" : "ja");
        return;
      }

      target = target.parentNode;
    }
  });
}());
