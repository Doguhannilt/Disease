// Data for the chart
const data = {
  labels: ["Hormonal Changes", "Stress and Anxiety", "Certain Foods and Beverages", "Lack of Sleep/Irregular Sleep Patterns", "Environmental Factors"],
  datasets: [{
    label: "Triggers for Migraine",
    data: [30, 25, 20, 15, 10], // Replace these values with real data
    backgroundColor: ["#f44336", "#ff9800", "#4caf50", "#2196f3", "#9c27b0"],
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
  const migraineTriggerChart = new Chart(document.getElementById("migraineTriggerChart"), config);
});
