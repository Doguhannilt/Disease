// Data for the chart
const data = {
  labels: ["Low Risk", "Moderate Risk", "High Risk"],
  datasets: [{
    label: "Risk of Progression",
    data: [20, 50, 30], // Replace these values with real data
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
const progressionChart = new Chart(document.getElementById("progressionChart"), config);
