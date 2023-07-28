// Data for the chart
const data = {
  labels: ["Sexual Contact", "Sharing Needles", "Mother to Child", "Contact with Infected Blood/Body Fluids"],
  datasets: [{
    label: "Risk Factors for Hepatitis B",
    data: [35, 25, 15, 25], // Replace these values with real data
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
  const hepatitisBRiskChart = new Chart(document.getElementById("hepatitisBRiskChart"), config);
});
