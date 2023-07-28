// Data for the chart
const data = {
  labels: ["Athlete's Foot", "Ringworm", "Candidiasis", "Aspergillosis", "Yeast Infections"],
  datasets: [{
    label: "Occurrences",
    data: [1200, 800, 600, 400, 300], // Replace these values with real data
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
const infectionChart = new Chart(document.getElementById("infectionChart"), config);
