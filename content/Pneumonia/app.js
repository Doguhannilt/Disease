// Data for the chart
const data = {
  labels: ["Bacterial Infections", "Viral Infections", "Fungal Infections", "Aspiration", "Smoking/Secondhand Smoke", "Age", "Weak Immune System"],
  datasets: [{
    label: "Causes and Risk Factors for Pneumonia",
    data: [20, 25, 15, 10, 15, 30, 20], // Replace these values with real data
    backgroundColor: ["#f44336", "#ff9800", "#4caf50", "#2196f3", "#9c27b0", "#673ab7", "#009688"],
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
  const pneumoniaRiskChart = new Chart(document.getElementById("pneumoniaRiskChart"), config);
});
