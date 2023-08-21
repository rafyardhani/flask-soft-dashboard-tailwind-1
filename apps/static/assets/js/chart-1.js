// chart 2

var ctx2 = document.getElementById("chart-line2").getContext("2d");

var gradientStroke1 = ctx2.createLinearGradient(0, 230, 0, 50);

gradientStroke1.addColorStop(1  , "rgba(246,208,171,1.000)");
gradientStroke1.addColorStop(0.2, "rgba(255, 232, 216, 0.2)");
gradientStroke1.addColorStop(0, "rgba(246,208,171,0)"); 
// gradientStroke1.addColorStop(0, ""); //purple colors

var gradientStroke2 = ctx2.createLinearGradient(0, 230, 0, 50);

gradientStroke2.addColorStop(1, "rgba(20,23,39,0.2)");
gradientStroke2.addColorStop(0.2, "rgba(72,72,176,0.0)");
gradientStroke2.addColorStop(0, "rgba(20,23,39,0)"); //purple colors

new Chart(ctx2, {
  type: "line",
  data: {
    labels: ["Mei", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Des","Jan","Feb","Mar","Apr"],
    datasets: [
      {
        label: "Hen Month Production",
        tension: 0.4,
        borderWidth: 1,
        pointRadius: 3,
        borderColor: "#FF6600",
        borderWidth: 3,
        backgroundColor: gradientStroke1,
        fill: true,
        data: [1.25, 1.35,  1.32,  1.31,  1.32,  1.31,  1.33,  1.36,  1.37,  1.36,  1.35,  1.33],
        
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
        datalables:{
          Anchor: 'end',
                align: 'top',
                formatter: Math.round,
                font: {
                    weight: 'bold',
                    size: 16
                },
        },
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
// [1.25, 1.35,  1.32,  1.31,  1.32,  1.31,  1.33,  1.36,  1.37,  1.36,  1.35,  1.33],