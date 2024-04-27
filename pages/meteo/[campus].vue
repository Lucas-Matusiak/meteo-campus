<template>
  <div class="mb-8" v-if="isLoading">
    <SkeletonMeteo />
  </div>
  <div
    v-else
    class="h-auto flex flex-col justify-center items-center w-[1000px]"
  >
    <div class="grid grid-cols-5 gap-4 grid-auto-flow:row">
      <!--GRID DEBUT -->

      <div
        class="bg-gradient-to-br from-[#2A8EAD] to-[#77c1d8] rounded-2xl shadow-md text-white col-span-3 row-span-3"
      >
        <!--GRID 1 -->

        <h1 class="text-1xl font-bold p-7">
          {{ route.params.campus }}
        </h1>
        <div class="flex items-center justify-around p-5">
          <div v-if="!isLoading && weatherData.current_weather">
            <Temperature :temperature="weatherData.current_weather.temperature"
              :feelsLike="weatherData.current_weather.feels_like_value" />
          </div>

          <div v-if="weatherData.current_weather.code">
            <WeatherIcon :code="weatherData.current_weather.code" size="large" />
          </div>

          <div v-if="weatherData && weatherData.current_weather">
            <Soleil :heureLever="weatherData.current_weather.sun_rise"
              :heureCoucher="weatherData.current_weather.sun_set" />
          </div>
        </div>
      </div>

      <div
        class="bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-2xl shadow-md text-white p-4 col-span-1"
      >
        <!-- GRID 2 HUMIDITE -->
        <div v-if="weatherData && weatherData.current_weather && weatherData.current_weather.humidity">
          <Humidite :humidite="weatherData.current_weather.humidity" />
        </div>
      </div>
      <div
        class="bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-2xl shadow-md text-white p-4 col-span-1"
      >
        <!-- GRID 3 VITESSE VENT -->
        <div v-if="weatherData && weatherData.current_weather && weatherData.current_weather.wind_speed">
          <VitesseVent :vitesseVent="weatherData.current_weather.wind_speed" />
        </div>
      </div>

      <div
        class="bg-gradient-to-tl from-[#9394F3] to-[#48A1EB] rounded-2xl shadow-md text-white p-4 col-span-2 row-span-2"
      >
        <!-- GRID 4 ACCESSOIRE ET VETEMENT -->
        <div>
          <AccessoireTenue />
        </div>
      </div>
    </div>

    <div
      class="bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-3xl my-5 shadow-lg"
      v-if="weatherData && weatherData.hourly_forecast"
    >
      <h1
        class="text-center text-white font-bold border-b border-white px-4 m-4"
        style="margin-top: 4px; margin-bottom: 4px"
      >
        Prévisions Heure par Heure
      </h1>
      <div class="flex overflow-x-scroll max-w-[400px] md:max-w-[1000px]">
        <!-- Utilisez une boucle v-for pour afficher les données de prévisions horaires -->
        <AffichageHeure v-for="(data, index) in weatherData.hourly_forecast" :key="index" :heure="data.time"
          :temperature="data.temperature" :pourcentagePluie="data.precipitation_proba" :vitesseVent="data.wind_speed"
          :code="data.code" />
      </div>
    </div>
    <div
      class="bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-3xl mb-4 shadow-lg l-[100%] w-[1000px]"
      v-if="weatherData && weatherData.hourly_forecast"
    >
      <h1
        class="text-center text-white font-bold m-4 px-4 border-b-0 md:border-b border-white"
        style="margin-top: 4px; margin-bottom: 4px"
      >
        Prévisions de la semaine
      </h1>
      <div class="flex flex-col md:flex-row md:w-[1000px]">
        <!-- Utilisez une boucle v-for pour afficher les données de prévisions horaires -->
        <AffichageJours v-for="(data, index) in weatherData.daily_forecast" :key="index" :date="data.date"
          :temperature="data.temperature_day" :min="data.temperature_min" :max="data.temperature_max"
          :vitesseVent="data.wind_speed_kmh" :code="data.code" />
      </div>
    </div>
  </div>

  <div>
    <!-- Bouton pour revenir à l'accueil -->
    <nuxt-link :to="`/universities/${selectedCampus}`"
      class="mt-7 pl-5 pr-5 bg-[#469FBB] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out">
      Retour à l'accueil
    </nuxt-link>
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import axios from "axios";

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
    //console.log("Contenu de la requête WEATHER:", response.data); // Affichage du contenu de la requête dans la console
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
