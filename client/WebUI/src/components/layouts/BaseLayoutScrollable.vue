<script setup lang="ts">
import Navigation from "@/components/navAndBanners/Navigation.vue";
import Footer from "@/components/navAndBanners/Footer.vue";
</script>

<template>
  <!-- This is the default layout used by 90% of the site. Content is relative
    (as oppoesd to fixed) and flows vertically as per a normal site -->
  <v-app>
    <div class="nav-wrapper">
      <Navigation />
    </div>
    <div class="promotional-banner-wrapper"></div>
    <!--Main-->
    <div class="main-content">
      <slot> </slot>
    </div>
    <div class="footer">
      <Footer />
    </div>
  </v-app>
</template>

<style scoped lang="scss">
.main-content {
  flex: 1 0 auto;
}

.promotional-banner-wrapper {
  z-index: 2;
  position: relative;
}

.nav-wrapper {
  z-index: 1;
}

.footer {
  position: relative;
}
</style>
