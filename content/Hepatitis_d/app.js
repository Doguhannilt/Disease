// Data for the chart
const data = {
  labels: ["Co-infection with Hepatitis B", "Contact with Infected Blood/Body Fluids"],
  datasets: [{
    label: "Risk Factors for Hepatitis D",
    data: [60, 40], // Replace these values with real data
    backgroundColor: ["#f44336", "#ff9800"],
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
  const hepatitisDRiskChart = new Chart(document.getElementById("hepatitisDRiskChart"), config);
});
