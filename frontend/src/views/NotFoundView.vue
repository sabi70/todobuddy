<template>
  <v-conatiner
    fluid
    class="d-flex justify-center align-center"
    id="status-code-404-container"
  >
    <img
      :src="require('@/assets/status_code_404_1.png')"
      id="status-404-img"
      @contextmenu.prevent
      @mousedown.prevent
    />
  </v-conatiner>
</template>
<script>
export default {
  name: "NotFound",
};
</script>
<style>
/* Handle responsive NotFoundView with media queries */
#status-404-img {
  min-width: 300px;
  max-width: 65%;
  user-select: none;
  -webkit-user-drag: none;
  -webkit-user-select: none;
}
/* Breakpoint: x < 768px */
@media screen and (max-width: 768px) {
  #status-code-404-container {
    padding-top: 20%;
  }
}
/* Breakpoint: x > 768px */
@media screen and (min-width: 768px) {
  #status-code-404-container {
    padding-top: 10%;
  }
}
/* Breakpoint: x > 992px */
@media screen and (min-width: 992px) {
  #status-code-404-container {
    padding-top: 10%;
  }
}
/* Breakpoint: x > 1200px */
@media screen and (min-width: 1200px) {
  #status-code-404-container {
    padding-top: 0%;
  }
}
</style>
