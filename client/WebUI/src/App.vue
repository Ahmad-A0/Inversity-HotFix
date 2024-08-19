<script setup lang="ts">
/*
Our top level App.vue component is the entry point for our Vue application. It is the parent component that wraps all other components in the application.
It is also the component where we define the router view that will render the components for the different routes in our application.

Look at the views in the /src/views folder to see the components that will be rendered by the router view.
*/
</script>

<template>
  <RouterView v-slot="{ Component }">
    <component :is="Component" :key="$route.path + $route.params"></component>
  </RouterView>
</template>

<style lang="scss"></style>