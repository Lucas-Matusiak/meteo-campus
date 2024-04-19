<template>
  <div v-if="isLoading">
    <SkeletonMeteo />
  </div>
  <div v-else class="h-auto flex flex-col justify-center items-center">
    <h1 class="text-1xl font-bold text-center mb-2">
      {{ route.params.campus }}
    </h1>
    <div class="flex">
      <div
        class="flex flex-col items-center justify-center bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-lg shadow-md w-full max-w-md mx-auto p-4 md:p-6 mr-6 mb-4">
        <div v-if="!isLoading && weatherData.current_weather"
          class="items-center justify-center pb-5 text-lg text-bold">
          <Temperature :temperature="weatherData.current_weather.temperature"
            :feelsLike="weatherData.current_weather.feels_like_value" />
        </div>
        <div v-if="weatherData &&
        weatherData.current_weather &&
        weatherData.current_weather.code
        ">
          <weather :code="weatherData.current_weather.code" />
        </div>
        <div v-if="weatherData && weatherData.current_weather">
          <Soleil :heureLever="weatherData.current_weather.sun_rise"
            :heureCoucher="weatherData.current_weather.sun_set" />
        </div>
      </div>
    </div>
    
    <div
    >
      <AccessoireTenue />
    </div>
    <div
      v-if="
        weatherData &&
        weatherData.current_weather &&
        weatherData.current_weather.humidity &&
        weatherData.current_weather.wind_speed
        ">
      <HumiditeVitesseDuVent :humidite="weatherData.current_weather.humidity"
        :vitesseVent="weatherData.current_weather.wind_speed" />
    </div>

    <div
      class="bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-3xl my-5 shadow-lg w-[60%] "
      v-if="weatherData && weatherData.hourly_forecast"
    >
      <h1
        class="text-center text-white font-bold border-b border-white px-4 m-4"
        style="margin-top: 4px; margin-bottom: 4px"
      >
        Prévisions Heure par Heure
      </h1>
      <div class="flex overflow-x-scroll max-w-[600px]">
        <!-- Utilisez une boucle v-for pour afficher les données de prévisions horaires -->
        <AffichageHeure v-for="(data, index) in weatherData.hourly_forecast" :key="index" :heure="data.time"
          :imgMeteo="data.weather_description" :temperature="data.temperature"
          :pourcentagePluie="data.precipitation_proba" :vitesseVent="data.wind_speed" />
      </div>
    </div>
    <!-- Bouton pour revenir à l'accueil -->
  </div>
  <nuxt-link
      :to="`/universities/${selectedCampus}`"
      class="mt-7 pl-5 pr-5 bg-[#469FBB] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out"
    >
      Retour à l'accueil
    </nuxt-link>
</template>

<script setup>
import { useRoute } from "vue-router";
import axios from "axios";
import AffichageHeure from "~/components/affichage-heure.vue";
import Temperature from "~/components/temperature.vue";
import HumiditeVitesseDuVent from "~/components/humidite-vitesse-vent.vue";
import SkeletonMeteo from "~/components/skeleton-meteo.vue";
import AccessoireTenue from "~/components/accessoire-tenue.vue";



const route = useRoute();
const selectedCampus = route.params.campus;

let weatherData = ref("");
let lat = ref("");
let lon = ref("");

let isLoading = computed(() => {
  return weatherData.value ? false : true;
});
// Appel de la méthode pour récupérer les données météorologiques
const api_call_weather = async () => {
  const request = `http://127.0.0.1:5000/api/complete_weather?lat=${lat.value}&lon=${lon.value}`;
  console.log(request);
  try {
    const response = await axios.get(request);
    console.log("Contenu de la requête WEATHER:", response.data); // Affichage du contenu de la requête dans la console
    weatherData.value = response.data; // Stockage des données météorologiques dans weatherData
  } catch (error) {
    console.error(
      "Erreur lors de la récupération des données météorologiques :",
      error
    );
  }
};

const api_call_localisation = async () => {
  try {
    const request = `http://127.0.0.1:5000/api/campus_localisation?campus=${selectedCampus}`;

    const encoded = encodeURI(
      `http://127.0.0.1:5000/api/campus_localisation?campus=${encodeURI(
        selectedCampus
      )}`
    );
    const response = await axios.get(encoded);

    lat.value = response.data[0].latitude;
    lon.value = response.data[0].longitude;
    console.log(lat.value);
    console.log(lon.value);
  } catch (error) {
    console.error(
      "Erreur lors de la récupération des localisations du campus :",
      error
    );
  }
};

await api_call_localisation();

if (lat.value && lon.value) {
  api_call_weather();
}
</script>
