// Data for the chart
const data = {
  labels: ["Age", "Obesity", "Joint Injuries/Repetitive Stress", "Family History", "Gender"],
  datasets: [{
    label: "Risk Factors for Osteoarthritis",
    data: [30, 25, 20, 15, 10], // Replace these values with real data
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
  const osteoarthritisRiskChart = new Chart(document.getElementById("osteoarthritisRiskChart"), config);
});
