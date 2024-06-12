// script.js

const texts = [
  "cout<<'Hola mundo!';",
  "System.out.println('Hola Mundo!');",
  "console.log('Hola Mundo!');",
  "print('Hola Mundo!');",
  "pip install Django",
  "npx create-react-app myapp",
  "npx create-next-app@latest my-next-app",
];

document.addEventListener("DOMContentLoaded", () => {
  const typewriterElement = document.getElementById("typewriter");
  let currentTextIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  const typingSpeed = 100;
  const erasingSpeed = 50;
  const newTextDelay = 2000;

  function type() {
    const currentText = texts[currentTextIndex];

    if (isDeleting) {
      typewriterElement.textContent = currentText.substring(0, charIndex - 1);
      charIndex--;
      if (charIndex === 0) {
        isDeleting = false;
        currentTextIndex = (currentTextIndex + 1) % texts.length;
        setTimeout(type, typingSpeed);
      } else {
        setTimeout(type, erasingSpeed);
      }
    } else {
      typewriterElement.textContent = currentText.substring(0, charIndex + 1);
      charIndex++;
      if (charIndex === currentText.length) {
        isDeleting = true;
        setTimeout(type, newTextDelay);
      } else {
        setTimeout(type, typingSpeed);
      }
    }
  }

  setTimeout(type, newTextDelay + 250);

  // Manejo de la activación de elementos <li>
  const menuItems = document.querySelectorAll(".menu li");
  menuItems.forEach((item) => {
    item.addEventListener("click", () => {
      event.preventDefault();
      menuItems.forEach((i) => i.classList.remove("active"));
      item.classList.add("active");
    });
  });
});
