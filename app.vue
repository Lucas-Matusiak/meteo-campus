<template>
  <div class="flex justify-center items-center flex-col mx-10">
    <img
      src="~/../assets/images/logo.png"
      alt="Description de l'image"
      class="w-20 h-auto mx-4"
    />
    <NuxtPage />

    <div class="flex items-center justify-center bg-white py-4">
      <div class="flex space-x-4">
        <button class="button">Nous contacter</button>
        <button class="button">Mentions légales</button>
        <button class="button">Nos réseaux</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
// Ajoutez ici vos variables réactives le cas échéant
</script>

<style scoped>
/* Aucun style spécifique nécessaire, car Tailwind est utilisé directement dans les classes HTML */
</style>
