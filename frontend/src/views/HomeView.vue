<template>
  <!-- 
    The page's permission: [IsAuthenticated];
    The authentication method: [BasicAuthentication];
   -->
  <div class="home" v-if="isAuthenticated">
    <v-card class="pa-4 text-center mb-5" title="🎯️ Create New Task 🎯️">
      <v-form v-model="isValid">
        <div id="task-creation-form">
          <v-text-field
            v-model="task.title"
            label="Title"
            :rules="[(value) => !!value || 'Please, fill the field!']"
          >
            <template v-slot:append-inner v-if="task.title.length != 0">
              <v-icon icon="mdi-close" @click="task.title = ''"></v-icon>
            </template>
          </v-text-field>
          <v-btn
            size="large"
            color="info"
            :disabled="!isValid"
            @click="createTask"
            block
          >
            Create
          </v-btn>
        </div>
      </v-form>
    </v-card>
    <v-snackbar v-model="snackbar">
      The operation was successfully done!
      <template v-slot:actions>
        <v-btn variant="text" color="green" @click="snackbar = false">
          close
        </v-btn>
      </template>
    </v-snackbar>
    <div id="task-container">
      <v-card
        variant="tonal"
        id="task-card"
        v-for="item in taskList"
        :key="item.pk"
        :title="item.title"
        target="_blank"
        subtitle="Check out the official repositary"
      >
        <template v-slot:prepend>
          <v-icon
            icon="mdi-check"
            color="success"
            @click="deleteTask(item.pk, true)"
          ></v-icon>
        </template>
        <template v-slot:append>
          <v-icon
            icon="mdi-delete"
            color="red-darken-1"
            @click="deleteTask(item.pk, false)"
          ></v-icon>
        </template>
      </v-card>
    </div>
  </div>
  <div v-if="!isAuthenticated">
    <AuthRequiredView></AuthRequiredView>
  </div>
</template>
<script>
// Used axios for fetching data from backend;
import axios from "axios";
import AuthRequiredView from "@/components/AuthRequired.vue";

export default {
  name: "HomeView",
  components: {
    AuthRequiredView,
  },
  data() {
    return {
      TASK_API_URL: "http://192.168.1.115:8000/tasks/",
      STATISTIC_UPDATING_URL: "http://192.168.1.115:8000/auth/user/statistic/",
      snackbar: false,
      isValid: false,
      taskList: [],
      task: {
        title: "",
      },
    };
  },
  methods: {
    // Methods for API interaction: GET, POST, PUT, DELETE;
    // method: POST
    async createTask() {
      try {
        const response = await axios.post(
          this.TASK_API_URL,
          {
            title: this.task.title,
          },
          {
            headers: {
              Authorization:
                "Basic " +
                btoa(
                  this.userCredentials.user +
                    ":" +
                    this.userCredentials.password
                ),
            },
          }
        );
        if (response.status == 201) {
          this.task.title = "";
          this.snackbar = true;
          this.getTask();
        } else {
          console.log("90");
        }
      } catch (err) {
        console.log(err);
      }
    },
    // method: GET
    async getTask() {
      try {
        const response = await axios.get(this.TASK_API_URL, {
          headers: {
            Authorization:
              "Basic " +
              btoa(
                this.userCredentials.user + ":" + this.userCredentials.password
              ),
          },
        });
        this.taskList = response.data;
      } catch (err) {
        console.log(err);
      }
    },
    // method: PUT
    async updateUserStatistic(status) {
      try {
        const response = await axios.put(
          this.STATISTIC_UPDATING_URL,
          {
            completed: status,
            not_completed: !status,
          },
          {
            headers: {
              Authorization:
                "Basic " +
                btoa(
                  this.userCredentials.user +
                    ":" +
                    this.userCredentials.password
                ),
            },
          }
        );
        if (response.status == 200) {
          /* Hello World! */
        }
      } catch (err) {
        console.log(err);
      }
    },
    // method: DELETE
    async deleteTask(pk, status) {
      try {
        const response = await axios.delete(
          this.TASK_API_URL + String(pk) + "/",
          {
            headers: {
              Authorization:
                "Basic " +
                btoa(
                  this.userCredentials.user +
                    ":" +
                    this.userCredentials.password
                ),
            },
          }
        );
        if (response.status == 204) {
          await this.updateUserStatistic(status);
          await this.getTask();
          this.snackbar = true;
        }
      } catch (err) {
        console.log(err);
      }
    },
  },
  computed: {
    // Checking if user is authenticated, getting stored data from cookies;
    isAuthenticated() {
      const authStatus = this.$cookies.get("isAuthenticated");
      return authStatus;
    },
    // Getting user credentials from vuex store
    userCredentials() {
      return this.$store.state.userCredentials;
    },
  },
  async mounted() {
    // Making API call in mounted lifecycle hook
    await this.getTask();
  },
};
</script>
<style scoped>
#task-container {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  gap: 1em;
}
@media screen and (max-width: 992px) {
  #task-container {
    display: inline-flex;
  }
  #task-card {
    width: 100%;
  }
}
</style>
