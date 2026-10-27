/* OEM browser-only example: one steady first-law residual, not EnerLint.
   No network calls; the demo makes no claim of independent validation. */
(() => {
  "use strict";
  const form = document.getElementById("wb-demo-form");
  if (form) {
    const defaults = { flow: 2, hin: 700000, hout: 500000, work: 400000, heat: 0 };
    const fields = Object.fromEntries(Object.keys(defaults).map(key => [key, form.elements.namedItem(key)]));
    const status = document.getElementById("wb-demo-status");
    const value = document.getElementById("wb-demo-result");
    const message = document.getElementById("wb-demo-message");
    const brokenCase = document.getElementById("wb-demo-break");
    const fmt = new Intl.NumberFormat("en-US", { maximumFractionDigits: 4 });

    const update = () => {
      const vals = {};
      for (const key of Object.keys(fields)) {
        const text = fields[key].value.trim();
        const num = Number(text);
        if (!text || !Number.isFinite(num)) {
          status.dataset.kind = "invalid";
          status.textContent = "□ INVALID INPUT";
          value.textContent = "r = —";
          message.textContent = "Enter finite numerical values in the stated SI units. Nothing was checked.";
          return;
        }
        vals[key] = num;
      }
      if (vals.flow < 0) {
        status.dataset.kind = "invalid";
        status.textContent = "□ INVALID INPUT";
        value.textContent = "r = —";
        message.textContent = "Mass flow must be a nonnegative magnitude at the declared inlet and outlet.";
        return;
      }
      const r = vals.flow * (vals.hin - vals.hout) + vals.heat - vals.work;
      if (!Number.isFinite(r)) {
        status.dataset.kind = "invalid";
        status.textContent = "□ INVALID INPUT";
        value.textContent = "r = —";
        message.textContent = "The calculation exceeds the supported numeric range.";
        return;
      }
      const clean = Object.is(r, -0) ? 0 : r;
      const pass = Math.abs(clean) <= 1;
      status.dataset.kind = pass ? "pass" : "fail";
      status.textContent = pass ? "● PASS · DEMO ONLY" : "▲ FAIL · DEMO ONLY";
      value.textContent = "r = " + fmt.format(clean) + " W";
      message.textContent = pass
        ? "The energy residual is within the 1 W demonstration threshold. Nothing else was evaluated."
        : "The energy residual exceeds the 1 W demonstration threshold. Check the declared values, signs and boundary.";
    };

    form.addEventListener("input", update);
    form.addEventListener("submit", event => event.preventDefault());
    form.addEventListener("reset", () => {
      for (const [key, def] of Object.entries(defaults)) fields[key].value = String(def);
      update();
    });
    brokenCase?.addEventListener("click", () => {
      for (const [key, def] of Object.entries(defaults)) fields[key].value = String(def);
      fields.work.value = String(defaults.work + 10000);
      update();
      fields.work.focus();
    });
    update();
  }

  const mobileMenu = document.querySelector(".wb-mobile-menu");
  if (mobileMenu) {
    mobileMenu.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", () => { mobileMenu.open = false; });
    });
    mobileMenu.addEventListener("keydown", event => {
      if (event.key === "Escape") {
        mobileMenu.open = false;
        mobileMenu.querySelector("summary")?.focus();
      }
    });
    if (window.matchMedia) {
      const desktop = window.matchMedia("(min-width: 831px)");
      desktop.addEventListener?.("change", event => {
        if (event.matches) mobileMenu.open = false;
      });
    }
  }
})();
