// $(document).ready(function() {
var options = {
    series: [
    {
      name: "",
      data: [1.25, 1.35,  1.32,  1.31,  1.32,  1.31,  1.33,  1.36,  1.37,  1.36,  1.35,  1.33]
    },
    {
      name: "",
      data: [null,null ,  1.32,  1.31,  null,  1.31,  null,  null,  null,  1.36,  1.35,  1.33]
    }
  ],
    chart: {
    height: 290,
    type: 'line',
    // dropShadow: {
    //   enabled: true,
    //   color: '#000',
    //   top: 18,
    //   left: 7,
    //   blur: 10,
    //   opacity: 0.2
    // },
    toolbar: {
      show: false
    }
  },
  colors: ['#AEA4A4', 'red'],
  dataLabels: {
    enabled: true,
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
    size: 1
  },
  xaxis: {
    categories: ['Mei-2021', 'Jun-2021', 'Jul-2021', 'Aug-2021', 'Sep-2021', 'Okt-2021', 'Nov-2021', 'Des-2021','Jan-2022','Feb-2022','Mar-2022','Apr-2022'],
    title: {
      text: 'Tanggal (Bulan)'
    }
  },
  yaxis: {
    min: 1.2,
    max: 1.4,
    tickAmount:4,
    // forceNiceScale: true,
    

    title: {
      text: 'Feed Conversation Ratio'
    }
  //   title: {
  //     text: 'Feed Converstion Ratio'
  //   },
  //   min: 20,
  //   tickAmount:4,
  //   max: 40
  },
  legend: {
    position: 'top',
    horizontalAlign: 'right',
    floating: true,
    offsetY: -25,
    offsetX: -5
  },
 
  };

  var chart = new ApexCharts(document.querySelector("#chartfcr"), options);
  chart.render();
  // fetch('/api/get_fcr_data')
  // .then(response => response.json())
  // .then(data => {
  //   // const categories = data.map(entry => entry.Bulan);
  //   const monthYearValues = data.map(entry => {
  //     const [year, month] = entry.Bulan.split('-');
  //     const monthName = new Date(year, month - 1).toLocaleString('en-us', { month: 'long' });
  //     return `${monthName} ${year}`;
  //   });
  //   const fcrValues = data.map(entry => entry.FCR);

  //   console.log(fcrValues, 'fcrValues')

  //   options.series = [
  //     {
  //       name: 'fcValues',
  //       data: fcrValues
  //     }
  //   ];
    
  //   options.xaxis.categories = monthYearValues;
  //     console.log(options, 'ngeents')
  
    
    
  //   var chart = new ApexCharts(document.querySelector("#chartfcr"), options);
  //   chart.render();
  // })
  
  // .catch(error => {
  //   console.error('Error fetching FCR data:', error);
  // });
// });
// });


