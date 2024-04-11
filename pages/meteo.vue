<template>
  <div class="h-auto flex flex-col justify-center items-center">
    <h1 class="text-3xl font-bold text-center mb-4">Météo Campus</h1>
    
    <!-- Composant Temperature -->
    <div class="items-center justify-center pb-5">
      <div>
        <p class="text-center text-2xl f bg-clip-text text-transparent bg-gradient-to-l from-black to-black">{{ temperature }}°C</p>
        <p class="text-center text-1xl bg-clip-text text-transparent bg-gradient-to-b from-black to-black">Ressenti {{ feelsLike }}°C</p>
      </div>
    </div>
    
    <div class=" "> <!-- Météo  -->
      <div>
        <weather/>
      </div>
      <div>
        <HumiditeVitesseDuVent/>
      </div>
      <div>
        <Soleil/>
      </div>

      <!-- Bouton pour revenir à l'accueil -->
      <nuxt-link to="/" class="ml-10 pl-20 pr-20 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out">
        Retour à l'accueil
      </nuxt-link>
    </div>

  </div>
</template>

<script>
// Importation de la bibliothèque Axios pour effectuer des requêtes HTTP
import axios from 'axios';

export default {
  name: 'Meteo', // Nom du composant Meteo
  data() {
    return {
      temperature: null, // Initialisation de la température à null
      feelsLike: null, // Initialisation de la température ressentie à null
    };
  },
  mounted() {
    this.getWeatherData(); // Appel de la méthode getWeatherData() lors du montage du composant
  },
  methods: {
    getWeatherData() {
      const apiUrl = 'http://localhost:5000/current_weather'; // URL de votre API
      const lat = 'your_lat'; // Remplacez par votre latitude
      const lon = 'your_lon'; // Remplacez par votre longitude
      axios.get(apiUrl, {
          params: {
            lat: lat,
            lon: lon
          }
        })
        .then(response => {
          // Récupération des données de température et température ressentie depuis la réponse de l'API
          this.temperature = response.data.temperature;
          this.feelsLike = response.data.feels_like_value;
        })
        .catch(error => {
          // Gestion des erreurs lors de la récupération des données météorologiques
          console.error('Erreur lors de la récupération des données météorologiques:', error);
        });
    }
  }
};
</script>

<style scoped>
/* Vos styles CSS personnalisés ici */
</style>
