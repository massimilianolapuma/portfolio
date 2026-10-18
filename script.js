document.getElementById("year").textContent = new Date().getFullYear();

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const toggles = [...document.querySelectorAll(".sound-toggle[data-video]")];

const setSound = (toggle, on) => {
  const video = document.getElementById(toggle.dataset.video);
  video.muted = !on;
  if (on && video.paused) video.play();
  toggle.setAttribute("aria-pressed", String(on));
  toggle.querySelector("b").textContent = on ? "Disattiva audio" : "Attiva audio";
};

toggles.forEach((toggle) => {
  toggle.addEventListener("click", () => {
    const on = toggle.getAttribute("aria-pressed") !== "true";
    // Only one video plays sound at a time.
    if (on) toggles.forEach((other) => other !== toggle && setSound(other, false));
    setSound(toggle, on);
  });
});

const inviewVideos = document.querySelectorAll("video[data-inview]");

if (reduceMotion) {
  // Show the poster frames until the visitor asks for playback.
  inviewVideos.forEach((video) => {
    video.removeAttribute("autoplay");
    video.pause();
  });
} else {
  // Play only while on screen: saves bandwidth and CPU, and the off-screen video falls silent.
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(({ target, isIntersecting }) => {
        if (isIntersecting) target.play().catch(() => {});
        else target.pause();
      });
    },
    { threshold: 0.4 },
  );
  inviewVideos.forEach((video) => observer.observe(video));
}
