<template>
  <div
    v-if="isLoading"
    class="max-w-sm animate-pulse flex flex-col justify-center items-center mt-8"
  >
    <div id="spinner" class="mb-10">
      <svg
        aria-hidden="true"
        class="inline w-10 h-10 text-gray-200 animate-spin dark:text-gray-600 fill-gray-600 dark:fill-gray-300"
        viewBox="0 0 100 101"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
          fill="currentColor"
        />
        <path
          d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
          fill="currentFill"
        />
      </svg>
    </div>

    <div
      role="status"
      class="space-y-8 md:space-y-8 rtl:space-x-reverse md:flex md:items-center flex-col"
    >
      <div
        class="flex items-center justify-center w-full h-48 bg-gray-300 rounded sm:w-96 dark:bg-gray-600"
      >
        <svg
          class="w-10 h-10 text-gray-200 dark:text-gray-600"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="currentColor"
          viewBox="0 0 20 18"
        >
          <path
            d="M18 0H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm4.376 10.481A1 1 0 0 1 16 15H4a1 1 0 0 1-.895-1.447l3.5-7A1 1 0 0 1 7.468 6a.965.965 0 0 1 .9.5l2.775 4.757 1.546-1.887a1 1 0 0 1 1.618.1l2.541 4a1 1 0 0 1 .028 1.011Z"
          />
        </svg>
      </div>

      <div class="w-full">
        <div
          class="h-2.5 bg-gray-200 rounded-full dark:bg-gray-600 w-48 mb-4"
        ></div>
        <div
          class="h-2 bg-gray-200 rounded-full dark:bg-gray-600 max-w-[480px] mb-2.5"
        ></div>
        <div class="h-2 bg-gray-200 rounded-full dark:bg-gray-600 mb-2.5"></div>
        <div
          class="h-2 bg-gray-200 rounded-full dark:bg-gray-600 max-w-[440px] mb-2.5"
        ></div>
        <div
          class="h-2 bg-gray-200 rounded-full dark:bg-gray-600 max-w-[460px] mb-2.5"
        ></div>
        <div
          class="h-2 bg-gray-200 rounded-full dark:bg-gray-600 max-w-[360px]"
        ></div>
      </div>

      <div class="w-full">
        <div
          class="h-2.5 bg-gray-200 rounded-full dark:bg-gray-600 max-w-[640px] mb-2.5 mx-auto"
        ></div>
        <div
          class="h-2.5 mx-auto bg-gray-200 rounded-full dark:bg-gray-600 max-w-[540px]"
        ></div>
      </div>
    </div>
  </div>
  <div v-else class="h-auto flex flex-col justify-center items-center w-full">
    <h1 class="text-1xl font-bold text-center mb-2">
      {{ route.params.campus }}
    </h1>
    <div
      v-if="!isLoading && weatherData.current_weather"
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
      class="bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-3xl mb-4 shadow-lg w-[50%]"
      v-if="weatherData && weatherData.hourly_forecast"
    >
      <h1
        class="text-center text-white font-bold border-b border-white px-4 m-4"
        style="margin-top: 4px; margin-bottom: 4px"
      >
        Prévisions Heure par Heure
      </h1>
      <div class="flex overflow-x-scroll">
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
