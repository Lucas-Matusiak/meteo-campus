<template>
  <div class="items-center justify-center">

    <div >
      <p v-if=temperature class="text-center text-2xl bg-clip-text text-transparent bg-gradient-to-l from-black to-black">{{ temperature }}°C</p>
      <p v-if=feelsLike class="text-center text-1xl bg-clip-text text-transparent bg-gradient-to-b from-black to-black">Ressenti {{ feelsLike }}°C</p>
    </div>
  </div>
</template>

<script setup>
  // Déclaration des variables et importation de defineProps
  import { defineProps } from 'vue';

  // Définition des propriétés du composant
  const props = defineProps({
    temperature: { type: Number, default: null },
    feelsLike: { type: Number, default: null }
  });
</script>

<style scoped>
/* Styles CSS spécifiques au composant ici */
</style>
