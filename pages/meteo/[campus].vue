<template>
  <div class="h-auto flex flex-col justify-center items-center">
    <h1 class="text-1xl font-bold text-center mb-2">
      {{ route.params.campus }}
    </h1>
    <div
      v-if="weatherData && weatherData.current_weather"
      class="items-center justify-center pb-5"
    >
      <Temperature
        :temperature="weatherData.current_weather.temperature"
        :feelsLike="weatherData.current_weather.feels_like_value"
      />
    </div>
    <div
      v-if="
        weatherData &&
        weatherData.current_weather &&
        weatherData.current_weather.code
      "
    >
      <weather :code="weatherData.current_weather.code" />
    </div>
    <div
      v-if="
        weatherData &&
        weatherData.current_weather &&
        weatherData.current_weather.humidity &&
        weatherData.current_weather.wind_speed
      "
    >
      <HumiditeVitesseDuVent
        :humidite="weatherData.current_weather.humidity"
        :vitesseVent="weatherData.current_weather.wind_speed"
      />
    </div>
    <div v-if="weatherData && weatherData.current_weather">
      <Soleil
        :heureLever="weatherData.current_weather.sun_rise"
        :heureCoucher="weatherData.current_weather.sun_set"
      />
    </div>

    <div
      class="bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-3xl mb-4 shadow-lg"
    >
      <h1
        class="text-center text-white font-bold border-b border-white px-4 m-4"
        style="margin-top: 4px; margin-bottom: 4px"
      >
        Prévisions Heure par Heure
      </h1>
      <div class="flex" v-if="weatherData && weatherData.hourly_forecast">
        <!-- Utilisez une boucle v-for pour afficher les données de prévisions horaires -->
        <AffichageHeure
          v-for="(data, index) in weatherData.hourly_forecast"
          :key="index"
          :heure="data.time"
          :imgMeteo="data.weather_description"
          :temperature="data.temperature"
          :pourcentagePluie="data.precipitation_proba"
          :vitesseVent="data.wind_speed"
        />
      </div>
    </div>
    <!-- Bouton pour revenir à l'accueil -->
    <nuxt-link
      :to="`/universities/${selectedCampus}`"
      class="pl-20 pr-20 bg-[#469FBB] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out"
    >
      Retour à l'accueil
    </nuxt-link>
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import axios from "axios";
import AffichageHeure from "~/components/affichage-heure.vue";
import Temperature from "~/components/temperature.vue";
import HumiditeVitesseDuVent from "~/components/humidite-vitesse-vent.vue";

//meteo aujourd'hui
let weatherData = ref(""); // Données météorologiques

const lat = "70.9623280";
const lon ="-37.23116682" ;

// Appel de la méthode pour récupérer les données météorologiques
onMounted(async () => {
  try {
    // Appel à l'API pour obtenir les données
    const response = await axios.get("http://127.0.0.1:5000/api/complete_weather", { params: { lat, lon } });
    console.log("Contenu de la requête:", response.data); // Affichage du contenu de la requête dans la console
    weatherData.value = response.data; // Stockage des données météorologiques dans weatherData
  } catch (error) {
    console.error(
      "Erreur lors de la récupération des données météorologiques :",
      error
    );
  }
});

//meteo heure par heure
const route = useRoute();
const selectedCampus = route.params.campus;
</script>
