<template>
    <div>
        <line-chart :height="200" :chart-data="statsData" :name="name"></line-chart>
    </div>
</template>

<script>
    import LineChart from './charts/LineChart.js'

    export default {
        props: ['stats', 'name'],
        data() {
            return {
                statsData: {
                    labels: this.stats,
                    datasets: [
                        {
                        label: this.name,
                        backgroundColor: '#e1dff7',
                        data: this.stats,
                        }
                    ]
                }
            }
        },
        components: {
            LineChart
        }
    }
</script>

<style>
</style>