<template>
  <!-- 
    Mobile and Desktop versions of about page.
    breakpoint for mobile: x < 992px
    breakpoint for desktop: x > 992px
   -->
  <MobileProfileView v-if="windowWidth < 992"></MobileProfileView>
  <DesktopProfile v-if="windowWidth >= 992"></DesktopProfile>
</template>
<script>
import MobileProfileView from "@/components/MobileProfile.vue";
import DesktopProfile from "@/components/DesktopProfile.vue";

export default {
  name: "AboutView",
  components: {
    MobileProfileView,
    DesktopProfile,
  },
  data() {
    return {
      timelineItems: [
        {
          title: "Aim to your goals!",
          context: "Lorem ipsum dolor sit amet.",
          color: "deep-purple-lighten-1",
        },
      ],
    };
  },
  computed: {
    windowWidth() {
      return this.$vuetify.display.width;
    },
  },
};
</script>
<style></style>
