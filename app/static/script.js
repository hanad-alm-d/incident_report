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

// Templates per crime type
const templates = {
    "Theft - From a Retailer (Shoplift)":
        "At approximately {incident_time} on {date}, a theft occurred at ({specific_area}). " +
        "The incident was reported by {reported_by}. " +
        "The person(s) of interest is/are described as: {poi_description}. " +
        "{item_quantity} item(s) - {item_description} were stolen, valued at ${item_value}."
};

let activeTemplate = null;
const theftFields = document.getElementById("theft_fields");

// Replace placeholders
function fillTemplate(template, values) {
    return template.replace(/{(\w+)}/g, (_, key) => values[key] || `[${key}]`);
}

// Collect form values
function getFormValues() {
    const fields = [
        'date',
        'incident_time',
        'specific_area',
        'reported_by',
        'poi_description',
        'item_quantity',
        'item_description',
        'item_value'
    ];

    const values = {};

    fields.forEach(field => {
        const el = document.getElementById(field);
        if (el) {
            values[field] = el.value;
        }
    });

    return values;
}

// Update description field
function updateDescription() {
    if (!activeTemplate) return;

    const values = getFormValues();
    const text = fillTemplate(activeTemplate, values);

    document.getElementById('description').value = text;
}

// Crime selection handler
document.getElementById('crime_related_incidents').addEventListener('change', function () {

    const crimeType = this.value;

    // Show / hide theft fields
    if (crimeType === "Theft - From a Retailer (Shoplift)") {
        theftFields.style.display = "block";
    } else {
        theftFields.style.display = "none";
    }

    // Apply template
    if (templates[crimeType]) {
        activeTemplate = templates[crimeType];
        updateDescription();
    } else {
        activeTemplate = null;
        document.getElementById('description').value = '';
    }

});

// Live updates when fields change
[
 'date',
 'incident_time',
 'specific_area',
 'reported_by',
 'poi_description',
 'item_quantity',
 'item_description',
 'item_value'
].forEach(id => {
    const el = document.getElementById(id);
    if (el) {
        el.addEventListener('input', updateDescription);
    }
});

};
