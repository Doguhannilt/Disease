// Data for the chart
const data = {
  labels: ["Taking Too Much Insulin/Medication", "Skipping Meals/Not Eating Enough", "Intense Physical Activity", "Excessive Alcohol Consumption"],
  datasets: [{
    label: "Causes of Hypoglycemia",
    data: [40, 30, 20, 10], // Replace these values with real data
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
  const hypoglycemiaRiskChart = new Chart(document.getElementById("hypoglycemiaRiskChart"), config);
});
