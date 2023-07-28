// Function to generate random numbers within a range
function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

// Data for the chart
const data = {
  labels: ["Mild", "Moderate", "Severe"],
  datasets: [{
    label: "Risk of Complications",
    data: [getRandomNumber(10, 50), getRandomNumber(20, 60), getRandomNumber(30, 70)],
    backgroundColor: ["#f44336", "#ff9800", "#4caf50"],
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
const spondylosisChart = new Chart(document.getElementById("spondylosisChart"), config);
