
<template>
  <div class="h-auto flex flex-col justify-center items-center">
    <h1 class="text-4xl font-bold text-center mb-4">Prévisions météo</h1>
    <div class=" "> <!-- Météo  -->

      <div class="flex justify-center mt-4">
        <Temperature/>
      </div>
      <div> 
        <HumuditeVitesseDuVent/>
      </div>
     
    </div>
  
    <!-- Bouton pour revenir à l'accueil -->
    <nuxt-link to="/" class="px-6 py-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out">
      Retour à l'accueil
    </nuxt-link>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      weatherData: null
    };
  },
  mounted() {
    this.getWeatherData();
  },
  methods: {
    async getWeatherData() {
      const lat = 48.8566;
      const lon = 2.3522;
      const apiUrl = 'http://127.0.0.1:5000/weather_data';

      try {
        const response = await axios.get(apiUrl, {
          params: {
            lat: lat,
            lon: lon
          }
        });

        this.weatherData = response.data; // Stocke les données météorologiques dans weatherData
      } catch (error) {
        console.error('Erreur lors de la récupération des données météorologiques :', error);
      }
    }
  }
}
</script>