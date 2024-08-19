<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();
</script>

<template>
  <div class="nav-wrapper bg-primary">
    <div class="end-spacer"></div>
    <div class="logo-link" @click="() => router.push('/')" aria-label="Click this logo to return home">
      <img src="/images/full_logo.svg" alt="inversity logo" />
    </div>
    <div class="middle-spacer"></div>
    <div class="navbar-actions">
      <v-icon color="membership" @click="() => { }">mdi-account</v-icon>
      <span @click="() => { }" class="link-text" to="/profile">Hi User!</span>
      <v-btn color="secondary" class="login-button">
        <span class="login-text">
          Logout
        </span>
      </v-btn>
    </div>
    <div class="end-spacer"></div>
  </div>
</template>

<style scoped lang="scss">
.nav-wrapper {
  width: 100vw;
  height: $navbar-height-desktop;
  display: flex;
  align-items: center;
}

.logo-link {
  height: 100%;
  padding-bottom: $spacing-xxs;
  padding-top: $spacing-xxs;
  cursor: pointer;
}

.logo-link img {
  height: 100%;
  padding: 0.25em;
}

.middle-spacer {
  flex: 100 0 auto;
}

.link-text {
  cursor: pointer;

}

.link-text:hover {
  text-decoration: underline;
}

.navbar-actions {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  flex: 0 0 auto;
  gap: $spacing-sm;
}

.end-spacer {
  width: 10vw;
}

@media screen and (max-width: $breakpoint-md) {

  /*
  We use a narrower navbar on mobile
  */
  .nav-wrapper {
    height: $navbar-height-mobile;
  }

  .login-button {
    // important needed to overrwite vuetify styles and make smaller on mobile
    height: 25px !important;
  }

  .login-text {
    font-size: $font-size-xxs;
  }

  .link-text {
    font-size: $font-size-xs;
  }
}
</style>
