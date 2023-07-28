// Data for the chart
const data = {
  labels: ["Female Anatomy", "Sexual Activity", "Certain Birth Control Methods", "Menopause", "Urinary Tract Abnormalities"],
  datasets: [{
    label: "Causes and Risk Factors for UTI",
    data: [40, 25, 15, 20, 10], // Replace these values with real data
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
  const utiRiskChart = new Chart(document.getElementById("utiRiskChart"), config);
});
