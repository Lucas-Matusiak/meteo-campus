<template>
  <div class="h-auto flex flex-col justify-center items-center">
    <h1 class="text-4xl font-bold text-center mb-4">Infos météo</h1>
    <!-- Bouton pour revenir à l'accueil -->
    <nuxt-link to="/" class="px-6 py-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out">
      Retour à l'accueil
    </nuxt-link>
    <!-- Div pour ajouter de l'espace -->
    <div class="humidity-wind-speed-container">
      <!-- Affichage du composant HumuditéVitesseDuVent.vue avec les valeurs d'humidité et de vitesse du vent -->
      <HumuditéVitesseDuVent :humidite="humidite" :vitesseVent="vitesseVent" />
    </div>
  </div>
</template>

<script>
import HumuditéVitesseDuVent from "~/components/HumuditéVitesseDuVent.vue";

export default {
  components: {
    HumuditéVitesseDuVent
  },
  data() {
    return {
      humidite: 60, // Exemple de valeur d'humidité (en pourcentage)
      vitesseVent: 25 // Exemple de valeur de vitesse du vent (en km/h)
    };
  }
};
</script>

<style scoped>
.humidity-wind-speed-container {
  margin-top: 20px; /* Ajouter de l'espace au-dessus */
}
</style>
