<template>
  <div id="statistic-container" class="d-flex justify-center align-center">
    <Bar
      id="my-chart-id"
      :options="chartOptions"
      :data="chartData"
      class=""
    ></Bar>
  </div>
</template>
<script>
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

export default {
  name: "BarChart",
  components: { Bar },
  props: {
    completed: Number,
    notCompleted: Number,
    username: String,
  },
  data() {
    return {
      /* Chart's configurations */
      chartData: {
        labels: ["Completed", "Not Completed"],
        datasets: [
          {
            label: "Task Activity",
            data: [this.completed, this.notCompleted],
            backgroundColor: ["#00ff7f", "#ff6347"],
          },
        ],
      },
      chartOptions: {
        plugins: {
          legend: {
            display: false,
          },
          title: {
            display: true,
            text: "The activity of: " + this.username,
          },
        },
        responsive: true,
      },
    };
  },
  methods: {},
};
</script>
<style>
#statistic-container {
  max-height: 350px;
}
</style>
