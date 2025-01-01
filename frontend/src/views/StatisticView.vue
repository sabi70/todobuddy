<template>
  <!--Bar Chart-->
  <v-container>
    <v-card>
      <v-card-text>
        The chart with user's completed task count and not completed task count.
      </v-card-text>
      <div v-for="item in usersList" :key="item.pk">
        <div v-if="item.username == $route.params.username">
          <BarChart
            :completed="item.completed"
            :notCompleted="item.not_completed"
            :username="item.username"
          ></BarChart>
        </div>
      </div>
    </v-card>
  </v-container>
  <!--Doughnut Chart-->
  <v-container>
    <v-card>
      <v-card-text>The chart with users activity comparatively:</v-card-text>
      <div v-if="usersList">
        <DoughnutChart
          :usernames="usersList.map((item) => item.username)"
          :taskSum="
            usersList.map((item) =>
              item.completed + item.not_completed == 0
                ? 1
                : item.completed + item.not_completed
            )
          "
        ></DoughnutChart>
      </div>
    </v-card>
  </v-container>
</template>
<script>
import axios from "axios";
import BarChart from "@/components/BarChart.vue";
import DoughnutChart from "@/components/DoughnutChart.vue";

export default {
  name: "StatisticView",
  /* Bar Chart is for self user stats and Doughnut is for all users stats */
  components: {
    BarChart,
    DoughnutChart,
  },
  data() {
    return {
      USERS_LIST_URL: "http://192.168.1.115:8000/auth/users/all/",
      usersList: null,
      usernames: [],
      taskSum: [],
    };
  },
  methods: {
    /* API call that gets users Info (auth is not required: [AllowAny]) */
    async getUsers() {
      try {
        const response = await axios.get(this.USERS_LIST_URL);
        if (response.status == 200) {
          const apiData = response.data;
          this.usersList = apiData;
          this.usernames = apiData.map((item) => item.username);
        }
      } catch (err) {
        console.log(err);
      }
    },
  },
  async mounted() {
    /* Making API call in mounted lifecycle hook */
    await this.getUsers();
  },
};
</script>
<style></style>
