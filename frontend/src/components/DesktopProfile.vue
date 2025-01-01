<template>
  <v-container fluid class="rounded-xl d-flex bg-info">
    <!-- Images are not selectable -->
    <v-img
      height="auto"
      :src="require('@/assets/user.png')"
      id="user-img"
      @contextmenu.prevent
      @mousedown.prevent
    >
    </v-img>
    <v-img
      class="mx-auto mb-0"
      height="auto"
      :src="require('@/assets/todo_logo_0.png')"
      id="todo-logo"
      @contextmenu.prevent
      @mousedown.prevent
    >
    </v-img>
  </v-container>
  <div>
    <v-timeline>
      <v-timeline-item
        v-for="(item, index) in timelineList"
        :key="index"
        :dot-color="item.color"
        fill-dot
        max-width="600"
      >
        <v-card class="pa-0">
          <v-card-title class="pa-0">
            <v-img
              :src="images[index]"
              class="align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(10,70,200,.6)"
              height="150px"
              cover
              @contextmenu.prevent
              @mousedown.prevent
            ></v-img>
          </v-card-title>
          <v-card-text class="font-weight-light">
            {{ quotations[index].quote }}
            <br />
            <p class="font-weight-medium">-{{ quotations[index].author }}</p>
          </v-card-text>
        </v-card>
      </v-timeline-item>
    </v-timeline>
  </div>
</template>
<script>
import dartboard from "@/assets/dartboard.png";
import calendar from "@/assets/calendar.png";
import progress from "@/assets/progress.png";

export default {
  name: "DesktopProfile",
  data() {
    return {
      // Imported images:
      images: [dartboard, calendar, progress],
      // Content of timeline items:
      quotations: [
        {
          author: "Bo Jackson",
          quote: "Set your goals high, and don't stop till you get there.",
        },
        {
          author: "Peter Drucker",
          quote: "What gets measured gets managed.",
        },
        {
          author: "George Bernard Shaw",
          quote:
            "Progress is impossible without change, and those who cannot change their minds cannot change anything.",
        },
      ],
      timelineList: [
        {
          title: "Aim to your goals!",
          context: "Lorem ipsum dolor sit amet.",
          color: "deep-purple-lighten-1",
          icon: "mdi-info",
        },
        {
          title: "Track your tasks!",
          context: "Lorem ipsum dolor sit amet.",
          color: "light-green-accent-3",
          icon: "",
        },
        {
          title: "Increase your productivity!",
          context: "Lorem ipsum dolor sit amet.",
          color: "pink-accent-3",
          icon: "",
        },
      ],
    };
  },
  computed: {
    themeMode() {
      return localStorage.getItem("theme");
    },
  },
};
</script>
<style>
#todo-logo {
  width: 100%;
  max-width: 350px;
}
</style>
