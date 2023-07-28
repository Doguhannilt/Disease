// Function to generate random numbers within a range
function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

// Data for the chart
const data = {
  labels: ["Mild", "Moderate", "Severe"],
  datasets: [{
    label: "Risk of Complications",
    data: [getRandomNumber(10, 40), getRandomNumber(20, 60), getRandomNumber(30, 80)],
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
const chickenpoxChart = new Chart(document.getElementById("chickenpoxChart"), config);
