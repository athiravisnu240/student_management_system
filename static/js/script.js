const navBtns = document.querySelectorAll(".nav-btn");
const targets = new Set();
// toggle navbars
navBtns.forEach((navBtn) => {
  targets.add(...document.querySelectorAll(navBtn.getAttribute("data-nav-to")));
  navBtn.addEventListener("click", (e) => {
    e.preventDefault();
    const targetSelector = navBtn.getAttribute("data-nav-to");
    const clickedTarget = document.querySelector(targetSelector);

    if (clickedTarget) {
      targets.forEach((target) => {
        if (target === clickedTarget) {
          target.classList.remove("d-none");
          target.classList.add("d-flex");
        } else {
          target.classList.remove("d-flex");
          target.classList.add("d-none");
        }
      });
    }
  });
});

// toggle forms
const formToggleBtn = document.getElementById("formToggleBtn");
const togglableForms = Array.from(document.querySelectorAll(".form-toggle"));

const capitalizeFirstLetter = (str) =>
  `${str.charAt(0).toUpperCase()}${str.slice(1)}`;

const toggleForms = (forms) => {
  let activeFormIndex = forms.findIndex((form) =>
    form.classList.contains("d-flex")
  );
  const nextFormIndex = (activeFormIndex + 1) % forms.length;

  forms.forEach((form, index) => {
    if (index === nextFormIndex) {
      form.classList.add("d-flex");
      form.classList.remove("d-none");
    } else {
      form.classList.remove("d-flex");
      form.classList.add("d-none");
    }
  });

  return forms[(nextFormIndex + 1) % forms.length];
};

if (formToggleBtn && togglableForms.length > 0) {
  formToggleBtn.addEventListener("click", (e) => {
    const nextForm = toggleForms(togglableForms);
    const formName = nextForm.getAttribute("id").replace("Form", "");
    e.target.textContent = capitalizeFirstLetter(formName);
  });
}

// Calendar
window.onload = function () {
  const calendars = document.querySelectorAll(".calendar");

  calendars.forEach(function (calendarEl) {
    var holidayDataAsString = calendarEl.getAttribute("data-calendar");
    var holidayDataAsStringUpdated = holidayDataAsString.replace(/'/g, '"');
    var holidayData = JSON.parse(holidayDataAsStringUpdated);

    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: "dayGridMonth",
      events: holidayData,
    });

    calendar.render();
  });
};
