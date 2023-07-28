// Data for the chart
const data = {
  labels: ["Mild", "Moderate", "Severe"],
  datasets: [{
    label: "Severity of Bronchial Asthma",
    data: [300, 500, 200], // Replace these values with real data
    backgroundColor: ["#4caf50", "#ff9800", "#f44336"],
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
const asthmaChart = new Chart(document.getElementById("asthmaChart"), config);
