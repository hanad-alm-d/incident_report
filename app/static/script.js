window.onload = function () {
  // Set default date and time
  const now = new Date();

  const dateVal = now.toISOString().split("T")[0];
  console.log("Setting date value to:", dateVal);
  document.getElementById("date").value = dateVal;

  const timeVal = now.toTimeString().split(" ")[0].substring(0, 5);
  console.log("Setting reported_time value to:", timeVal);
  document.getElementById("reported_time").value = timeVal;

  // Loading overlay functionality
  const submitButton = document.querySelector("input[type='submit']");
  const loadingOverlay = document.getElementById("loading-overlay");
  const form = document.querySelector("form");

  if (submitButton && loadingOverlay && form) {
    submitButton.addEventListener("click", function () {
      // Show overlay and disable button
      loadingOverlay.style.display = "flex";
      submitButton.disabled = true;
      submitButton.value = "Sending...";
    });

    // Optional: re-enable button if user somehow cancels (for AJAX or validation)
    form.addEventListener("reset", function () {
      loadingOverlay.style.display = "none";
      submitButton.disabled = false;
      submitButton.value = "Generate Report";
    });
  }
};
