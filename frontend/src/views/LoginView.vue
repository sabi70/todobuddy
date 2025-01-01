<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <v-responsive class="mx-auto" max-width="350">
          <v-card
            style="
              backdrop-filter: blur(10px);
              background-color: rgba(255, 255, 255, 0.2);
              box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
              border-radius: 10px;
            "
            :loading="requestLoading"
            class="pa-4 mt-4 mx-auto"
            title="User Log-in"
            variant="outlined"
          >
            <v-form v-model="isValid">
              <v-text-field
                hide-details="auto"
                label="Username"
                placeholder="Linus"
                prepend-icon="mdi-account"
                variant="underlined"
                v-model="username"
                counter="20"
                validate-on="input"
                required
                :rules="[
                  usernameRules.required,
                  usernameRules.whiteSpace,
                  usernameRules.nonWord,
                ]"
              ></v-text-field>
              <v-text-field
                hide-details="auto"
                label="Password"
                placeholder="qwerty"
                prepend-icon="mdi-lock"
                variant="underlined"
                v-model="password"
                :type="showPassword ? 'text' : 'password'"
                required
                :rules="[
                  passwordRules.required,
                  passwordRules.whiteSpace,
                  passwordRules.nonWord,
                ]"
              >
                <template v-slot:append>
                  <v-icon
                    :icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    @click="showPassword = !showPassword"
                  ></v-icon>
                </template>
              </v-text-field>
              <v-card color="surface-variant" variant="tonal" class="mt-6">
                <v-card-text class="text-medium-emphasis text-caption">
                  {{ rulesDescription }}
                </v-card-text>
              </v-card>
              <v-btn
                :disabled="!isValid"
                @click="login"
                color="info"
                class="mt-4"
                size="large"
                type="submit"
                block
              >
                login
              </v-btn>
            </v-form>
          </v-card>
        </v-responsive>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import store from "@/store";
import axios from "axios";

export default {
  name: "LoginView",
  data() {
    return {
      // Constant variables:
      LOGIN_URL: "http://192.168.1.115:8000/auth/login/",
      // Dynamic variables:
      showPassword: false,
      requestLoading: false,
      username: "",
      password: "",
      isValid: true,
      // The rules for username, search pattern is in RegExp:
      usernameRules: {
        required: (value) => !!value || "Please, fill the field!",
        whiteSpace: (value) =>
          !/\s/.test(value) || "The username must be without withespace!",
        nonWord: (value) =>
          !/[^a-zA-Z0-9_]/.test(value) ||
          "The username must be in Latin letters!",
      },
      // The rules for password, search pattern is in RegExp:
      passwordRules: {
        required: (value) => !!value || "Please, fill the field!",
        whiteSpace: (value) =>
          !/\s/.test(value) || "The password must be without withespace!",
        nonWord: (value) =>
          !/[^a-zA-Z0-9_]/.test(value) ||
          "The password must be in Latin letters!",
      },
      // The username and password creation tips:
      rulesDescription:
        "When you create an account use these standarts to make strong\
        username and secure password: number in password, at least one\
        upper case letter, at least one lower case letter, no whitespace,\
        min length of password must be greater than 4, max length of password\
        must be lower than 20, the letters of password must be in Latin.",
    };
  },
  methods: {
    // The authentication method that makes API post request, call to login registry
    async login() {
      // Checking if the rules of username and password fields are correct, if correct allow make request
      if (this.isValid == true) {
        this.requestLoading = true;
        // Try to make post request
        try {
          await axios
            .post(this.LOGIN_URL, {
              username: this.username,
              password: this.password,
            })
            .then((response) => {
              // Handling response of API call;
              // If response status is equal to 200
              //    store username and auth state in cookies
              //    update vuex storage with new values
              //    redirect the user to main page
              if (response.status == 200) {
                this.requestLoading = false;
                this.$cookies.set("user", this.username, "1d");
                this.$cookies.set("password", this.password, "1d");
                this.$cookies.set("isAuthenticated", true, "1d");
                store.dispatch("updateUser", {
                  user: this.username,
                  password: this.password,
                  isAuthenticated: true,
                });
                this.$router.push("/");
              } else {
                // If the response status code is not equal to 200
                // show alert dialog window with that error
                console.log(response.data.message);
              }
            });
          this.requestLoading = false;
        } catch (err) {
          // Catching errors of post request method
          console.log(err);
        }
      }
    },
  },
};
</script>
