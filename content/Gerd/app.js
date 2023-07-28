// Data for the chart
const data = {
  labels: ["Obesity", "Hiatal Hernia", "Pregnancy", "Smoking", "Trigger Foods/Beverages"],
  datasets: [{
    label: "Risk Factors for GERD",
    data: [25, 20, 15, 10, 30], // Replace these values with real data
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
window.addEventListener('DOMContentLoaded', (event) => {
  const gerdRiskChart = new Chart(document.getElementById("gerdRiskChart"), config);
});
