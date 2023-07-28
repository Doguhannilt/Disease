// Data for the chart
const data = {
  labels: ["Spinal Cord Injuries", "Stroke", "Brain Injuries/Tumors", "Neurological Disorders", "Peripheral Nerve Injuries"],
  datasets: [{
    label: "Causes of Paralysis",
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
  const paralysisRiskChart = new Chart(document.getElementById("paralysisRiskChart"), config);
});
