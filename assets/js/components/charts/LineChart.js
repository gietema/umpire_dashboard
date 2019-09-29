import { Line, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Line,
  mixins: [reactiveProp],
  props: ['chartData', 'options'],
  mounted () {
    // this.chartData is created in the mixin.
    // If you want to pass options please create a local options object
    this.renderChart(this.chartData, {
        maintainAspectRatio: false,
        scales:{
            xAxes: [{
                display: false //this will remove all the x-axis grid lines
            }]
        },
        legend: {
            display: false
        },
    })
  }
}