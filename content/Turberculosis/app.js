// Data for the chart
const data = {
  labels: ["Close Contact with Infected Person", "Crowded Living/Working Conditions", "Weakened Immune System", "Malnutrition", "Age", "Substance Abuse"],
  datasets: [{
    label: "Risk Factors for Tuberculosis",
    data: [25, 20, 30, 15, 10, 15], // Replace these values with real data
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
  const tbRiskChart = new Chart(document.getElementById("tbRiskChart"), config);
});
