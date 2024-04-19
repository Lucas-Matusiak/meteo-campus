<template>
  <div class="flex flex-col">

    <div v-if="temperature !== null && feelsLike !== null">
      <p class="text-6xl bg-clip-text text-white font-bold py-2 ">{{ temperature }}°C</p>
      <p class="text-sm bg-clip-text text-white">Ressenti
        <span class="text-center text-1xl bg-clip-text text-white font-bold"> {{ feelsLike }}°C</span>
      </p> 
    </div>
   
    <div v-else>
      <p>Loading...</p>
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
