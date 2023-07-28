// Data for the chart
const data = {
  labels: ["Age", "Gender", "Pregnancy", "Family History", "Obesity", "Prolonged Sitting/Standing"],
  datasets: [{
    label: "Causes and Risk Factors for Varicose Veins",
    data: [30, 40, 20, 25, 15, 20], // Replace these values with real data
    backgroundColor: ["#f44336", "#ff9800", "#4caf50", "#2196f3", "#9c27b0", "#673ab7"],
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
  const varicoseVeinsRiskChart = new Chart(document.getElementById("varicoseVeinsRiskChart"), config);
});
