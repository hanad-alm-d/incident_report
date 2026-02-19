window.onload = function () {
  const now = new Date();

  const dateVal = now.toISOString().split("T")[0];
  console.log("Setting date value to:", dateVal);
  document.getElementById("date").value = dateVal;

  const timeVal = now.toTimeString().split(" ")[0].substring(0, 5);

  console.log("Setting reported_time value to:", timeVal);
  document.getElementById("reported_time").value = timeVal;
};
