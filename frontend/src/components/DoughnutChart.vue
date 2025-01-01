<template>
  <div class="d-flex align-center justify-center">
    <Doughnut :data="data" :options="options"></Doughnut>
  </div>
</template>
<script>
import { Doughnut } from "vue-chartjs";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
ChartJS.register(ArcElement, Tooltip, Legend);

export default {
  name: "DoughnutChart",
  components: {
    Doughnut,
  },
  props: {
    usernames: Array,
    taskSum: Array,
  },
  data() {
    return {
      /* Chart's configurations */
      data: {
        labels: this.usernames,
        datasets: [
          {
            backgroundColor: [
              "#1abc9c",
              "#9b59b6",
              "#d35400",
              "#34495e",
              "#f1c40f",
              "#3498db",
              "#c0392b",
              "#16a085",
              "#f39c12",
              "#2c3e50",
              "#e74c3c",
            ],
            data: this.taskSum,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: "bottom",
          },
        },
      },
    };
  },
};
</script>
<style>
canvas {
  width: auto;
  height: auto;
}
</style>
