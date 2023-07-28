// Data for the chart
const data = {
  labels: ["Type A", "Type B", "Type C", "Type D", "Type E", "Type F"],
  datasets: [{
    label: "Types of Drug Reactions",
    data: [20, 15, 10, 8, 5, 7], // Replace these values with real data
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
const drugReactionsChart = new Chart(document.getElementById("drugReactionsChart"), config);
