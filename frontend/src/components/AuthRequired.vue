<template>
  <!-- Auth required view for not AUTHENTICATED users -->
  <v-conatiner
    fluid
    class="d-flex justify-center align-center"
    id="login-required-container"
  >
    <!-- Making the image not selectable -->
    <img
      :src="require('@/assets/login_required.png')"
      id="login-required-img"
      @contextmenu.prevent
      @mousedown.prevent
    />
  </v-conatiner>
</template>
<script>
export default {
  name: "AuthRequiredView",
};
</script>
<style>
#login-required-img {
  min-width: 300px;
  max-width: 65%;
  user-select: none;
  -webkit-user-drag: none;
  -webkit-user-select: none;
}
/* Media queries for responsive design */
@media screen and (max-width: 768px) {
  #login-required-container {
    padding-top: 20%;
  }
}
@media screen and (min-width: 768px) {
  #login-required-container {
    padding-top: 10%;
  }
}
@media screen and (min-width: 992px) {
  #login-required-container {
    padding-top: 10%;
  }
}
@media screen and (min-width: 1200px) {
  #login-required-container {
    padding-top: 0%;
  }
}
</style>
