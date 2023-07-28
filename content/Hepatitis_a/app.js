// Data for the chart
const data = {
  labels: ["Inadequate Handwashing", "Contaminated Food/Water", "Travel to High-Risk Regions", "Close Quarters with Infected Individuals"],
  datasets: [{
    label: "Risk Factors for Hepatitis A",
    data: [30, 40, 10, 20], // Replace these values with real data
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
  const hepatitisARiskChart = new Chart(document.getElementById("hepatitisARiskChart"), config);
});
