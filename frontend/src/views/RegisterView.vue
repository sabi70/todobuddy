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
            title="User Registration"
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
                  usernameRules.minLength,
                  usernameRules.whiteSpace,
                  usernameRules.nonWord,
                  usernameRules.maxLength,
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
                  passwordRules.maxLength,
                  passwordRules.minLength,
                  passwordRules.numberRequired,
                  passwordRules.whiteSpace,
                  passwordRules.upperCase,
                  passwordRules.lowerCase,
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
                @click="register"
                color="info"
                class="mt-4"
                size="large"
                type="submit"
                block
              >
                sign-in
              </v-btn>
            </v-form>
          </v-card>
        </v-responsive>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import axios from "axios";

export default {
  name: "RegisterView",
  data() {
    return {
      // Constant variables:
      REGISTER_URL: "http://192.168.1.115:8000/auth/register/",
      // Dynamic vaiables:
      showPassword: false,
      requestLoading: false,
      username: "",
      password: "",
      isValid: true,
      // The rules for username, search pattern in RegExp:
      usernameRules: {
        required: (value) => !!value || "Please, fill the field!",
        minLength: (value) =>
          value.length >= 4 || "Minimal length of username is 4",
        whiteSpace: (value) =>
          !/\s/.test(value) || "The username must be without withespace!",
        maxLength: (value) =>
          value.length <= 20 || "Maximal length of username is 20",
        nonWord: (value) =>
          !/[^a-zA-Z0-9_]/.test(value) ||
          "The username must be in Latin letters!",
      },
      // The rules for password, search patter in RegExp:
      passwordRules: {
        required: (value) => !!value || "Please, fill the field!",
        maxLength: (value) =>
          value.length <= 15 || "Maximal length of password is 15",
        minLength: (value) =>
          value.length >= 4 || "Minimal length of username is 4",
        numberRequired: (value) =>
          /\d/.test(value) || "Password must contain at least one number",
        whiteSpace: (value) =>
          !/\s/.test(value) || "The password must be without withespace!",
        upperCase: (value) =>
          /[A-Z]/.test(value) ||
          "The password must contain at least one Upper case!",
        lowerCase: (value) =>
          /[a-z]/.test(value) ||
          "The password must contain at least one lower case!",
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
    // The authentication method that makes post request call to register new user;
    register() {
      // Checking if the rules of username and password fields are correct, if correct allow make request
      if (this.isValid == true) {
        this.requestLoading = true;
        try {
          // Try make post reqeust to REGISTER_URL for user registration
          axios
            .post(this.REGISTER_URL, {
              username: this.username,
              password: this.password,
            })
            .then((response) => {
              // Handling the response of API call
              // If response status code is equal to 201(200) redirect to login page
              if (response.status == 201 || response.status == 200) {
                this.requestLoading = false;
                // redirect the user to the login page
                this.$router.push("/login");
              }
              // If response status code is equal to 226
              // Show logs that this user already has been registered
              // Show link of login page in alert dialog
              if (response.status == 226) {
                this.requestLoading = false;
                console.log(response.status);
              }
              // If response status code is equal to 400
              // show logs with that error
              if (response.status == 400) {
                this.requestLoading = false;
                console.log(response.status);
              }
            });
          this.requestLoading = !this.requestLoading;
        } catch (err) {
          // In all other cases show logs with err
          console.log(err);
        }
      }
    },
  },
};
</script>
