// Data for the chart
const data = {
  labels: ["Autoimmune Diseases", "Iodine Deficiency", "Thyroid Surgery/Radiation", "Certain Medications"],
  datasets: [{
    label: "Causes of Hypothyroidism",
    data: [40, 20, 15, 10], // Replace these values with real data
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
  const hypothyroidismRiskChart = new Chart(document.getElementById("hypothyroidismRiskChart"), config);
});
