<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>

<template>
  <div id="footer">
    <span class="copyright-message">© Inversity LTD 2024</span>
    <span class="spacer"></span>
    <span class="footer-links">
      <a target="_blank" href="https://forms.gle/Hqsyx47gJaH4J8CF7">Feedback</a>
    </span>
    <span class="footer-links">
      <a target="_blank" href="https://discord.gg/sX9GZEJ65n">Discord</a>
    </span>
    <span class="footer-links">
      <RouterLink to="/privacy-policy">Privacy policy</RouterLink>
    </span>
  </div>
</template>

<style lang="scss">
#footer {
  height: $footer-height;
  background: $theme-surface-darken-1;
  color: $theme-text;
  z-index: 2;
  font-size: $font-size-xxs;
  display: flex;
  flex-direction: row;
  align-items: center;
}

.copyright-message {
  padding-left: $spacing-sm;
}

.spacer {
  flex: 1 1 auto;
}

.footer-links {
  padding-right: $spacing-sm;
}
</style>
