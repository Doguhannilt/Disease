// Data for the chart
const data = {
  labels: ["Family History", "Obesity/Overweight", "Unhealthy Diet", "Lack of Physical Activity", "Smoking", "Chronic Stress"],
  datasets: [{
    label: "Risk Factors for Hypertension",
    data: [30, 40, 25, 35, 20, 15], // Replace these values with real data
    backgroundColor: ["#f44336", "#ff9800", "#4caf50", "#2196f3", "#9c27b0", "#ffc107"],
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
  const hypertensionRiskChart = new Chart(document.getElementById("hypertensionRiskChart"), config);
});
