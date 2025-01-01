<template>
  <v-container fluid id="about-container">
    <div class="rounded-xl">
      <v-card class="mx-auto" width="auto">
        <v-container class="bg-info d-flex justify-center pa-0">
          <v-img
            height="auto"
            :src="require('@/assets/user.png')"
            id="user-img"
            @contextmenu.prevent
            @mousedown.prevent
          >
          </v-img>
        </v-container>
        <v-card-text>
          <div class="font-weight-bold ms-1 mb-2">sabico</div>
        </v-card-text>
        <v-timeline align="start" density="compact" class="pl-2">
          <v-timeline-item
            v-for="(item, index) in aboutMeItems"
            :key="index"
            :dot-color="item.color"
            size="x-small"
          >
            <div class="mb-4">
              <div class="font-weight-normal">
                <strong>{{ item.title }}</strong>
              </div>
              <div>{{ item.context }}</div>
            </div>
          </v-timeline-item>
        </v-timeline>
      </v-card>
    </div>
    <div id="context-container">
      <v-card
        v-for="(item, index) in aboutMeItems"
        :key="index"
        class="mt-5"
        id="context-item"
      >
        <v-img
          :src="images[index]"
          class="align-end"
          gradient="to bottom, rgba(0,0,0,.1), rgba(10,70,200,.6)"
          height="200px"
          cover
          @contextmenu.prevent
          @mousedown.prevent
        >
          <v-card-title class="text-white">{{ item.title }}</v-card-title>
        </v-img>
        <v-card-text class="font-weight-light">
          {{ quotations[index].quote }}
          <br />
          <p class="font-weight-medium">-{{ quotations[index].author }}</p>
        </v-card-text>
      </v-card>
    </div>
  </v-container>
</template>
<script>
import dartboard from "@/assets/dartboard.png";
import calendar from "@/assets/calendar.png";
import progress from "@/assets/progress.png";

export default {
  name: "MobileProfileView",
  data() {
    return {
      images: [dartboard, calendar, progress],
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
      aboutMeItems: [
        {
          title: "Aim to your goals!",
          context: "Lorem ipsum dolor sit amet.",
          color: "deep-purple-lighten-1",
          path: "@/assets/dartboard.png",
        },
        {
          title: "Track your tasks!",
          context: "Lorem ipsum dolor sit amet.",
          color: "light-green-accent-3",
          path: "@/assets/calendar.png",
        },
        {
          title: "Increase your productivity!",
          context: "Lorem ipsum dolor sit amet.",
          color: "pink-accent-3",
          path: "@/assets/progress.png",
        },
      ],
    };
  },
};
</script>
<style>
#user-img {
  width: 100%;
  max-width: 350px;
  display: flex;
  justify-content: center;
  /*background: linear-gradient(to top, #00bcd4, white);*/
  /*background: conic-gradient(#00bcd4, white, #00bcd4);*/
}
@media (min-width: 768px) and (max-width: 992px) {
  #context-container {
    display: flex;
    gap: 5px;
  }
  #context-item {
    width: 33%;
  }
}
</style>
