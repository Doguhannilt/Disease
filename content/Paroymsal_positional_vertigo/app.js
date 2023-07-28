// Data for the chart
const data = {
  labels: ["Head Injury", "Inner Ear Infections", "Age-related Degeneration of Inner Ear", "Prolonged Bed Rest/Immobility"],
  datasets: [{
    label: "Risk Factors for Paroxysmal Positional Vertigo",
    data: [30, 25, 20, 15], // Replace these values with real data
    backgroundColor: ["#f44336", "#ff9800", "#4caf50", "#2196f3"],
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
  const ppvRiskChart = new Chart(document.getElementById("ppvRiskChart"), config);
});
