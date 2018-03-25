type = ['', 'info', 'success', 'warning', 'danger'];

loan_applications_graph = function(loan_applications_data){
  var dataEmailsSubscriptionChart = {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      series: [
          Object.values(loan_applications_data)
      ]
  };
  var optionsEmailsSubscriptionChart = {
      axisX: {
          showGrid: false
      },
      low: 0,
      high: 1000,
      chartPadding: {
          top: 0,
          right: 5,
          bottom: 0,
          left: 0
      }
  };
  var responsiveOptions = [
      ['screen and (max-width: 640px)', {
          seriesBarDistance: 5,
          axisX: {
              labelInterpolationFnc: function(value) {
                  return value[0];
              }
          }
      }]
  ];
  var emailsSubscriptionChart = Chartist.Bar('#emailsSubscriptionChart', dataEmailsSubscriptionChart, optionsEmailsSubscriptionChart, responsiveOptions);

  //start animation for the Emails Subscription Chart
  md.startAnimationForBarChart(emailsSubscriptionChart);
}

completed_applications_graph = function(completed_applications_data){
  dataCompletedTasksChart = {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      series: [
          Object.values(completed_applications_data)
      ]
  };

  optionsCompletedTasksChart = {
      lineSmooth: Chartist.Interpolation.cardinal({
          tension: 0
      }),
      low: 0,
      high: 500, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
      chartPadding: {
          top: 0,
          right: 0,
          bottom: 0,
          left: 0
      }
  }

  var completedTasksChart = new Chartist.Line('#completedTasksChart', dataCompletedTasksChart, optionsCompletedTasksChart);

  // start animation for the Completed Tasks Chart - Line Chart
  md.startAnimationForLineChart(completedTasksChart);
}

bank_share_prices = function(bank_share_prices_data){
  /* ----------==========     Daily Sales Chart initialization    ==========---------- */

  dataDailySalesChart = {
      labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S','M', 'T', 'W', 'T', 'F', 'S', 'S'],
      series: [
          bank_share_prices_data
      ]
  };

  optionsDailySalesChart = {
      lineSmooth: Chartist.Interpolation.cardinal({
          tension: 0
      }),
      low: 0,
      high: 200, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
      chartPadding: {
          top: 0,
          right: 0,
          bottom: 0,
          left: 0
      },
  }

  var dailySalesChart = new Chartist.Line('#dailySalesChart', dataDailySalesChart, optionsDailySalesChart);

  md.startAnimationForLineChart(dailySalesChart);
}
