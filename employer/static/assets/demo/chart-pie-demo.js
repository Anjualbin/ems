// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
        datasets: [{
          data: {{ data|safe }},
          backgroundColor: [
            '#696969', '#808080', '#A9A9A9', '#C0C0C0'
          ],
          label: 'Role'
        }],
        labels: {{ labels|safe }}
      },
      options: {
        responsive: true
      }
});
