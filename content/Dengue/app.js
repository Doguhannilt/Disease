// Function to generate random numbers within a range
function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

// Data for the chart
const data = {
  labels: ["Mild", "Moderate", "Severe"],
  datasets: [{
    label: "Severity of Dengue Symptoms",
    data: [getRandomNumber(10, 30), getRandomNumber(30, 60), getRandomNumber(50, 80)],
    backgroundColor: ["#4caf50", "#ff9800", "#f44336"],
    borderWidth: 1
  }]
};

// Chart configuration
const config = {
  type: 'bar',
  data: data,
  options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
};

// Create the chart
const dengueSeverityChart = new Chart(document.getElementById("dengueSeverityChart"), config);
