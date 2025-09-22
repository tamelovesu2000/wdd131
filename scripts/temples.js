// temples.js

// ✅ Dynamic footer year
const yearSpan = document.querySelector("#year");
const today = new Date();
yearSpan.textContent = today.getFullYear();

// ✅ Last modified date
const lastModified = document.querySelector("#lastModified");
lastModified.textContent = document.lastModified;

// ✅ Hamburger menu for mobile
const hamburgerBtn = document.querySelector("#hamburgerBtn");
const navMenu = document.querySelector("nav");

hamburgerBtn.addEventListener("click", () => {
  navMenu.classList.toggle("open");

  // Change button symbol
  if (hamburgerBtn.textContent === "☰") {
    hamburgerBtn.textContent = "✖";
  } else {
    hamburgerBtn.textContent = "☰";
  }
});
