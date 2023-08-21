// $(document).ready(function() {
    var options = {
        series: [
        {
          name: "   ",
          data: [8.96, 31.7, 20.4, 27.3, 29.21, 24.41, 31.93, 23.78, 24.87, 31.69, 22.56, 23.11]
        },
        {
        //   name: "Low - 2013",
          data: [null, null, 20.4, null, null, 24.41, null, 23.78, null, null, 22.56, null]
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
        size: 0
      },
      xaxis: {
        categories: ['Mei-2021', 'Jun-2021', 'Jul-2021', 'Aug-2021', 'Sep-2021', 'Okt-2021', 'Nov-2021', 'Des-2021','Jan-2022','Feb-2022','Mar-2022','Apr-2022'],
        title: {
          text: 'Tanggal (Bulan)'
        },
        
      },
      yaxis: {
        labels:{
            formatter: (value) => {
                return `${value} Juta`;
              },
        },
        // min: 1.2,
        // max: 1.5,
        // tickAmount:5,
        // forceNiceScale: true,
        
    
        title: {
          text:' Keuntungan'
        },
      //   title: {
      //     text: 'Feed Converstion Ratio'
      //   },
        min: 0,
        tickAmount:4,
        max: 40,
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
      
        
        
        var chart = new ApexCharts(document.querySelector("#chartkeuntungan"), options);
        chart.render();
      // })
      
      // .catch(error => {
      //   console.error('Error fetching HMP data:', error);
      // });
    // });
    
    
    