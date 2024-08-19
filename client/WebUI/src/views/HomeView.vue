<script setup lang="ts">
import BaseLayoutScrollable from "@/components/layouts/BaseLayoutScrollable.vue";

</script>

<template>
  <BaseLayoutScrollable>
    <v-sheet class="ma-sm pa-sm d-flex flex-column gap-sm" elevation="2">
      <h3>Welcome to the Inversity Web UI Template!</h3>
      <p>Hey there! We’ve crafted this template just for you to explore and experiment with the tech stack and layout
        that power our web frontend. Dive in and see what you can create!</p>

      <h4>What's Included?</h4>
      <v-container>
        <v-row>
          <v-col cols=12 md=6>
            <v-card color="background">
              <v-card-title>Our Tech Stack</v-card-title>
              <v-card-text>
                <h4>Get ready to tinker with some cool tools:</h4>
                <ul>
                  <li><strong>Vue 3</strong>: The framework that's all about building awesome interfaces.</li>
                  <li><strong>Vite</strong>: Your speedy build tool, because who likes waiting around?</li>
                  <li><strong>Vuetify</strong>: Our UI component library that's like a design playground.</li>
                  <li><strong>Vue Router</strong>: Navigate through your app with ease.</li>
                  <li><strong>Pinia</strong>: Manage your state like a pro.</li>
                  <li><strong>SCSS</strong>: Unleash some CSS wizardry with neat variables and more!</li>
                  <li><strong>Dockerfile/Docker Compose</strong>: Spin up your environment effortlessly.</li>
                </ul>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols=12 md=6>
            <v-card color="background">
              <v-card-title>Our Layout</v-card-title>
              <v-card-text>
                <p>Check out our layout magic! Use the <strong>&lt;BaseLayoutScrollable&gt;</strong> tags to wrap your
                  content
                  and get a sleek
                  scrollable layout with our standard header and footer. It’s like having a polished canvas ready for
                  your
                  creativity!</p>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols=12>
            <v-card color="background" class="style-card">
              <v-card-title class="style-card__title">Our Styles</v-card-title>
              <v-card-text>
                <p>Our Vuetify theme comes loaded with a palette of primary, secondary, and tertiary colours that you
                  can
                  easily tweak using SCSS variables. Go ahead, make it your own and bring your designs to life!</p>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>





    </v-sheet>
  </BaseLayoutScrollable>
</template>

<style scoped lang="scss">
.style-card {
  background-image: linear-gradient(to right, $theme-primary, $theme-secondary, $theme-tertiary);

  &__title {
    color: $theme-background;
  }

  p {
    color: $theme-background;
  }
}
</style>
