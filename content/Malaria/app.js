// Data for the chart
const data = {
  labels: ["Traveling to Malaria-Endemic Areas", "Not Using Mosquito Nets/Repellents", "Lack of Immunity in Non-Endemic Populations"],
  datasets: [{
    label: "Risk Factors for Malaria",
    data: [40, 30, 20], // Replace these values with real data
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
  const malariaRiskChart = new Chart(document.getElementById("malariaRiskChart"), config);
});
