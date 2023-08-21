// chart 2

var ctx2 = document.getElementById("chart-line").getContext("2d");

var gradientStroke1 = ctx2.createLinearGradient(0, 230, 0, 50);

gradientStroke1.addColorStop(1, "rgba(203,12,159,0.2)");
gradientStroke1.addColorStop(0.2, "rgba(72,72,176,0.0)");
gradientStroke1.addColorStop(0, "rgba(203,12,159,0)"); //purple colors

var gradientStroke2 = ctx2.createLinearGradient(0, 230, 0, 50);

gradientStroke2.addColorStop(1, "rgba(20,23,39,0.2)");
gradientStroke2.addColorStop(0.2, "rgba(72,72,176,0.0)");
gradientStroke2.addColorStop(0, "rgba(20,23,39,0)"); //purple colors

new Chart(ctx2, {
  type: "line",
  data: {
    labels: ["Mei-2021", "Jun-2021", "Jul-2021", "Aug-2021", "Sep-2021", "Okt-2021", "Nov-2021", "Des-2021","Jan-2022","Feb-2022","Mar-2022","Apr-2022"],
    datasets: [
      {
        label: "Hen Month Production",
        tension: 0.4,
        borderWidth: 1,
        pointRadius: 3,
        borderColor: "#cb0c9f",
        borderWidth: 3,
        backgroundColor: gradientStroke1,
        fill: true,
        data: [91.40, 100.92, 101.26, 100.42, 101.28, 101.00, 102.65, 104.47, 101.84,104.98,104.25,102.65],
        
        maxBarThickness: 6,
      },
      {
        // label: "Websites",
        // tension: 0.4,
        // borderWidth: 0,
        // pointRadius: 0,
        // borderColor: "#3A416F",
        // borderWidth: 3,
        // backgroundColor: gradientStroke2,
        // fill: true,
        // data: [30, 90, 40, 140, 290, 290, 340, 230, 400],
        // maxBarThickness: 6,
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false,
      },
    },
  
    interaction: {
      intersect: false,
      mode: "index",
    },
    scales: {
      y: {
        grid: {
          drawBorder: false,
          display: true,
          drawOnChartArea: true,
          drawTicks: false,
          borderDash: [5, 5],
        },
        ticks: {
          display: true,
          padding: 10,
          color: "#b2b9bf",
          font: {
            size: 11,
            family: "Open Sans",
            style: "normal",
            lineHeight: 2,
          },
        },
      },
      x: {
        grid: {
          drawBorder: false,
          display: false,
          drawOnChartArea: false,
          drawTicks: false,
          borderDash: [5, 5],
        },
        ticks: {
          display: true,
          color: "#b2b9bf",
          padding: 20,
          font: {
            size: 11,
            family: "Open Sans",
            style: "normal",
            lineHeight: 2,
          },
        },
      },
    },
  },
});

// end chart 2
// 