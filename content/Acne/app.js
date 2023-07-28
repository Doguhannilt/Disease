// Data for the chart
const data = {
  labels: ["High Risk", "Medium Risk", "Low Risk"],
  datasets: [{
    label: "Risk of Severe Acne",
    data: [5, 30, 65], // Replace these values with real data
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
const acneChart = new Chart(document.getElementById("acneChart"), config);
