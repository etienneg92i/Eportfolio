/*
 * Bascule FR/EN cote client, sans rechargement de page.
 *
 * Le contenu anglais vit dans `content.traduction_en` (source unique de
 * verite, cf. content.py) et arrive dans la page via un bloc
 * <script type="application/json" id="i18n-data"> genere par main.py
 * (`_i18n_payload`). Ce script lit ce bloc et, au clic sur #lang-toggle,
 * remplace le texte de chaque element `[data-i18n="chemin.dans.le.json"]`
 * par sa traduction ; le texte francais d'origine est mis de cote pour
 * revenir dessus sans re-render serveur. Le choix de langue est retenu en
 * `localStorage` (prefs par onglet du navigateur, jamais envoye au serveur).
 *
 * Partage par index.html et 404.html : meme bouton, meme mecanique.
 */
(function () {
    "use strict";

    var STORAGE_KEY = "lang";
    var root = document.documentElement;
    var dataScript = document.getElementById("i18n-data");

    var EN = {};
    try {
        EN = dataScript ? JSON.parse(dataScript.textContent) : {};
    } catch (e) {
        EN = {};
    }

    // Texte francais d'origine, mis de cote au premier passage sur chaque
    // element pour pouvoir y revenir sans re-render serveur.
    var originaux = new WeakMap();
    var titreOriginal = document.title;
    var descEl = document.querySelector('meta[name="description"]');
    var descOriginale = descEl ? descEl.getAttribute("content") : null;

    function lire(chemin) {
        var parts = chemin.split(".");
        var v = EN;
        for (var i = 0; i < parts.length; i++) {
            if (v == null) return undefined;
            v = v[parts[i]];
        }
        return typeof v === "string" ? v : undefined;
    }

    function appliquer(langue) {
        var versAnglais = langue === "en";

        document.querySelectorAll("[data-i18n]").forEach(function (el) {
            if (!originaux.has(el)) originaux.set(el, el.textContent);
            var traduit = versAnglais ? lire(el.getAttribute("data-i18n")) : undefined;
            el.textContent = traduit !== undefined ? traduit : originaux.get(el);
        });

        if (descEl) {
            var desc = versAnglais ? lire("profil.presentation") : undefined;
            descEl.setAttribute("content", desc !== undefined ? desc : descOriginale);
        }

        var cleTitre = document.body.getAttribute("data-i18n-title");
        var titre = versAnglais && cleTitre ? lire(cleTitre) : undefined;
        document.title = titre !== undefined ? titre : titreOriginal;

        root.lang = langue;
        root.setAttribute("data-lang", langue);

        var bouton = document.getElementById("lang-toggle");
        if (bouton) {
            bouton.textContent = versAnglais ? "FR" : "EN";
            bouton.setAttribute(
                "aria-label",
                versAnglais
                    ? (lire("ui.lang_toggle_to_fr") || "Passer en français")
                    : (lire("ui.lang_toggle_to_en") || "Switch to English")
            );
        }

        try {
            localStorage.setItem(STORAGE_KEY, langue);
        } catch (e) {
            // Stockage indisponible (navigation privee, quota...) : la
            // bascule reste utilisable, juste pas retenue au rechargement.
        }
    }

    function langueInitiale() {
        var stockee = null;
        try {
            stockee = localStorage.getItem(STORAGE_KEY);
        } catch (e) {
            stockee = null;
        }
        return stockee === "en" ? "en" : "fr";
    }

    document.addEventListener("DOMContentLoaded", function () {
        var bouton = document.getElementById("lang-toggle");
        if (bouton) {
            bouton.addEventListener("click", function () {
                appliquer(root.lang === "en" ? "fr" : "en");
            });
        }
        appliquer(langueInitiale());
    });
})();
