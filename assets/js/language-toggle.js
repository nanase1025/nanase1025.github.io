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

  document.addEventListener("DOMContentLoaded", function () {
    var toggles = document.querySelectorAll("[data-language-toggle]");

    Array.prototype.forEach.call(toggles, function (toggle) {
      toggle.addEventListener("click", function (event) {
        event.preventDefault();

        var current = document.documentElement.getAttribute("data-language");
        setLanguage(current === "ja" ? "en" : "ja");
      });
    });
  });
}());
