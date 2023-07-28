// Data for the chart
const data = {
  labels: ["Contaminated Water", "Undercooked/Raw Meat", "Person-to-Person Contact"],
  datasets: [{
    label: "Risk Factors for Hepatitis E",
    data: [50, 30, 20], // Replace these values with real data
    backgroundColor: ["#f44336", "#ff9800", "#4caf50"],
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
  const hepatitisERiskChart = new Chart(document.getElementById("hepatitisERiskChart"), config);
});
