<template>
  <div class="items-center justify-center">

    <!-- Utilisation de v-if pour afficher le contenu lorsque weatherData est disponible -->
    <div v-if="weatherData">
      
      <p class="text-center text-2xl bg-clip-text text-transparent bg-gradient-to-l from-black to-black">{{ weatherData.temperature_value }}°C</p>
      <!-- Affiche la température provenant de weatherData -->

      <p class="text-center text-1xl bg-clip-text text-transparent bg-gradient-to-b from-black to-black">Ressenti {{ weatherData.feels_like_value }}°C</p>
      <!-- Affiche le ressenti provenant de weatherData -->
    </div>
   

    <!-- Utilisation de v-else pour afficher "Loading..." lorsque weatherData est null -->
    <div v-else>
      
      <p>Loading...</p>
      <!-- Affiche "Loading..." pendant le chargement des données -->
    </div>
    <!-- Fin du bloc de chargement -->
  </div>
</template>

<script>
// Définition du composant Vue.js
export default {
  // Déclaration des propriétés du composant
  props: {
    weatherData: { type: Object, default: null } // Propriété weatherData de type Object avec une valeur par défaut null
  }
};
</script>

<style scoped>
/* Styles CSS spécifiques au composant ici */
</style>
