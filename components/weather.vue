<template>
    <div class="mb-10" v-if="weatherData && weatherData.current_weather">
          <!-- Affichage conditionnel des images et descriptions basé sur le code météo -->
            <div v-if="weatherData.current_weather.code.toString().startsWith('2')">
                <img src="../assets/images/ensoleille.png" alt="soleil" class="content-center object-scale-down h-48 w-96">
                <h1 class="text-1xl text-center mb-4">Ensoleillé</h1>
            </div>          
            <div v-else-if="weatherData.current_weather.code.toString().startsWith('3')">
                <img src="../assets/images/ensoleille.png" alt="soleil" class="content-center object-scale-down h-48 w-96">
                <h1 class="text-1xl text-center mb-4">Ensoleillé</h1>
            </div> 
            <div v-else-if="npm install axios

            ">
                <img src="../assets/images/ensoleille.png" alt="soleil" class="content-center object-scale-down h-48 w-96">
                <h1 class="text-1xl text-center mb-4">Ensoleillé</h1>
            </div> 
            <div v-else-if="weatherData.current_weather.code.toString().startsWith('6')">
                <img src="../assets/images/ensoleille.png" alt="soleil" class="content-center object-scale-down h-48 w-96">
                <h1 class="text-1xl text-center mb-4">Ensoleillé</h1>
            </div> 
            <div v-else-if="weatherData.current_weather.code.toString().startsWith('7')">
                <img src="../assets/images/ensoleille.png" alt="soleil" class="content-center object-scale-down h-48 w-96">
                <h1 class="text-1xl text-center mb-4">Ensoleillé</h1>
            </div> 
            <div v-if="weatherData.current_weather.code.toString().startsWith('8') && weatherData.current_weather.code !== 800">
                <img src="../assets/images/ensoleille.png" alt="soleil" class="content-center object-scale-down h-48 w-96">
                <h1 class="text-1xl text-center mb-4">Ensoleillé</h1>
            </div>
            <div v-else-if="weatherData.current_weather.code == 800">
                <img src="../assets/images/ensoleille.png" alt="soleil" class="content-center object-scale-down h-48 w-96">
                <h1 class="text-1xl text-center mb-4">Ensoleillé</h1>
            </div> 
            <div >
            <h1 class="text-2xl  text-center mb-4"> {{ lieu }}</h1>
            </div>
          <!-- Ajoutez plus de conditions ici selon les groupes de codes météo -->
        </div>

</template>

<script>
import axios from 'axios';
export default {
  props: {
    lieu: { type: String, default: null },
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
      const lat = "14.499454";
      const lon ="-17.4440600" ;
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