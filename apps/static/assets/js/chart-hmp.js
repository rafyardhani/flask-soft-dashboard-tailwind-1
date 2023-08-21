// $(document).ready(function() {
var options = {
    series: [
    {
      name: " haha  ",
      data: [91.40, 100.92, 101.26, 100.42, 101.28, 101.00, 102.65, 104.47, 101.84,104.98,104.25,102.65]
    },
    {
      name: "Low - 2013",
      data: [null, null, null, 100.42,null, 101.00, null, null, 101.84,null,104.25,102.65]
    },
    
  ],
    chart: {
    height: 300,
    type: 'line',
    // dropShadow: {
    //   enabled: false,
    //   color: '#AEA4A4',
    //   top: 18,
    //   left: 7,
    //   blur: 10,
    //   opacity: 0.2
    // },
    toolbar: {
      show: false
    }
  },
  colors: ['#AEA4A4','red'],
  dataLabels: {
    enabled: true,
    // enabledOnSeries: [1],
  },
  stroke: {
    curve: 'smooth'
  },
  // title: {
  // //   text: 'Average High & Low Temperature',
  // //   align: 'left'
  // },
  // grid: {
  //   borderColor: '#e7e7e7',
  //   row: {
  //     colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
  //     opacity: 0.5
  //   },
  // },
  markers: {
    size: 0
  },
  xaxis: {
    categories: ['Mei-2021', 'Jun-2021', 'Jul-2021', 'Aug-2021', 'Sep-2021', 'Okt-2021', 'Nov-2021', 'Des-2021','Jan-2022','Feb-2022','Mar-2022','Apr-2022'],
    title: {
      text: 'Tanggal (Bulan)'
    }
  },
  yaxis: {
    // min: 1.2,
    // max: 1.5,
    // tickAmount:5,
    // forceNiceScale: true,
    labels:{
      formatter: (value) => {
          return `${value} %`;
        },
  },

    title: {
      text:' Hen Month Prodcution'
    },
  //   title: {
  //     text: 'Feed Converstion Ratio'
  //   },
    min: 90,
    tickAmount:4,
    max: 110,
  },
  legend: {
    position: 'top',
    horizontalAlign: 'right',
    floating: true,
    offsetY: -25,
    offsetX: -5
  },
 
  };

  // var chart = new ApexCharts(document.querySelector("#charthmp"), options);
//   chart.render();
  // fetch('/api/get_hmp_data')
  // .then(response => response.json())
  // .then(data => {
  //   // const categories = data.map(entry => entry.Bulan);
  //   const monthYearValues = data.map(entry => {
  //     const [year, month] = entry.Bulan.split('-');
  //     const monthName = new Date(year, month - 1).toLocaleString('en-us', { month: 'long' });
  //     return `${monthName} ${year}`;
  //   });
    
  //   const hmpValues = data.map(entry => entry.HMP);


  //   options.series = [
  //     {
  //       name: 'hmpValues',
  //       data: hmpValues
  //     }
  //   ];
    
  //   options.xaxis.categories = monthYearValues;
  //     // console.log(options, 'ngeents')
  
    
    
    var chart = new ApexCharts(document.querySelector("#charthmp"), options);
    chart.render();
  // })
  
  // .catch(error => {
  //   console.error('Error fetching HMP data:', error);
  // });
// });


