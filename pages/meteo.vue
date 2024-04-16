<template>
 
  <div class="h-auto flex flex-col justify-center items-center">
    <!-- Div principale avec des classes Tailwind CSS pour la mise en page -->
    <h1 class="text-3xl font-bold text-center mb-4">Météo Campus</h1>
    

    <!-- Début de la zone du composant Temperature.vue -->
    <div v-if="weatherData && weatherData.current_weather" class="items-center justify-center pb-5">
    <Temperature
      :temperature="weatherData.current_weather.temperature"
      :feelsLike="weatherData.current_weather.feels_like_value"/>
    </div>
    <!-- Section météo -->
    <div>
      <weather/>
    </div>
      
      <div>
        <HumiditeVitesseDuVent v-if="weatherData" :humidite="weatherData.current_weather.humidity" :vitesseVent="weatherData.current_weather.wind_speed" />
      </div>
  
      <div v-if="weatherData && weatherData.current_weather">
        <Soleil
        :heureLever="weatherData.current_weather.sun_rise"
        :heureCoucher="weatherData.current_weather.sun_set"/>
      </div>

      <!-- Bouton pour revenir à l'accueil -->
      <nuxt-link to="/" class="ml-10 pl-20 pr-20 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out">
        Retour à l'accueil
      </nuxt-link>
    </div>

  
</template>

<script>
// Import des modules nécessaires
import axios from 'axios';
import Temperature from '~/components/Temperature.vue'; // Import du composant Temperature.vue
import HumiditeVitesseDuVent from '~/components/HumiditeVitesseDuVent.vue';

export default {
  components: {
    Temperature,
    HumiditeVitesseDuVent,   // Utilisation du composant Temperature.vue
  },
  data() {
    // Initialisation des données
    return {
      weatherData: null, // Données météorologiques
    };
  },
  mounted() {
    // Appel de la méthode pour récupérer les données météorologiques
    this.getWeatherData();
  },
  methods: {
    async getWeatherData() {
      // Paramètres de latitude et longitude
      const lat = "70.9623280";
      const lon ="-37.23116682" ;
      // URL de l'API pour les données météorologiques
      const apiUrl = 'http://127.0.0.1:5000/complete_weather';

      try {
        // Appel à l'API pour obtenir les données
        const response = await axios.get(apiUrl, { params: { lat, lon } });
        console.log('Contenu de la requête:', response.data); // Affichage du contenu de la requête dans la console
        this.weatherData = response.data; // Stockage des données météorologiques dans weatherData

      } catch (error) {
        console.error('Erreur lors de la récupération des données météorologiques :', error); // Gestion des erreurs
      }
    }
  }
}
</script>

<style scoped>
/* Styles CSS spécifiques au composant ici */
</style>
