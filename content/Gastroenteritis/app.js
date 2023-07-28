// Data for the chart
const data = {
  labels: ["Viral Infections", "Bacterial Infections", "Parasitic Infections", "Contaminated Food/Water", "Close Contact", "Poor Hygiene"],
  datasets: [{
    label: "Risk Factors for Gastroenteritis",
    data: [30, 25, 10, 20, 15, 5], // Replace these values with real data
    backgroundColor: ["#f44336", "#ff9800", "#4caf50", "#2196f3", "#9c27b0", "#00bcd4"],
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
  const gastroenteritisRiskChart = new Chart(document.getElementById("gastroenteritisRiskChart"), config);
});
