document.getElementById("year").textContent = new Date().getFullYear();

const manifesto = document.getElementById("manifesto-video");
const soundToggle = document.getElementById("sound-toggle");

if (manifesto && soundToggle) {
  // Respect reduced-motion: show the poster frame until the visitor asks for playback.
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    manifesto.removeAttribute("autoplay");
    manifesto.pause();
  }

  soundToggle.addEventListener("click", () => {
    const soundOn = manifesto.muted;
    manifesto.muted = !soundOn;
    if (soundOn && manifesto.paused) manifesto.play();
    soundToggle.setAttribute("aria-pressed", String(soundOn));
    soundToggle.querySelector("b").textContent = soundOn ? "Disattiva audio" : "Attiva audio";
  });
}
