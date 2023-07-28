// Function to generate random numbers within a range
function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

// Data for the chart
const data = {
  labels: ["Family History", "Obesity", "Sedentary Lifestyle", "High Blood Pressure", "High Cholesterol", "PCOS", "Age"],
  datasets: [{
    label: "Risk Factors for Diabetes",
    data: [getRandomNumber(10, 40), getRandomNumber(20, 60), getRandomNumber(30, 70), getRandomNumber(10, 40), getRandomNumber(10, 30), getRandomNumber(10, 40), getRandomNumber(10, 40)],
    backgroundColor: ["#f44336", "#ff9800", "#4caf50", "#2196f3", "#9c27
