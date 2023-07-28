// Data for the chart
const data = {
  labels: ["Injection Drug Use", "Blood Transfusion (prior to screening)", "Unprotected Sexual Contact", "Mother to Child"],
  datasets: [{
    label: "Risk Factors for Hepatitis C",
    data: [40, 30, 15, 5], // Replace these values with real data
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
  const hepatitisCRiskChart = new Chart(document.getElementById("hepatitisCRiskChart"), config);
});
