// Data for the chart
const data = {
  labels: ["Straining", "Constipation", "Pregnancy", "Obesity", "Prolonged Sitting"],
  datasets: [{
    label: "Risk Factors for Hemorrhoids",
    data: [30, 40, 20, 25, 15], // Replace these values with real data
    backgroundColor: ["#f44336", "#ff9800", "#4caf50", "#2196f3", "#9c27b0"],
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
const hemorrhoidsRiskChart = new Chart(document.getElementById("hemorrhoidsRiskChart"), config);
