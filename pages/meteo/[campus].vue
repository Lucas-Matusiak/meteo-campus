<template>
  <div class="h-auto flex flex-col justify-center items-center">
    <h1 class="text-3xl font-bold text-center mb-4">Météo Campus</h1>
    <div class=" ">
      <!-- Météo  -->
      <p>{{ route.params.campus }}</p>
      <div>
        <Temperature />
        <weather />
      </div>
      <div></div>
      <div>
        <HumiditeVitesseDuVent />
      </div>
      <div>
        <Soleil />
      </div>
      <div
        class="bg-gradient-to-r from-blue-300 to-indigo-500 rounded-3xl mb-4"
      >
      <h1
        class="text-center text-white font-bold border-b border-white px-4 m-4"
        style="margin-top: 4px; margin-bottom: 4px"
      >
        Prévisions Heure par Heure
      </h1>
      <div class="flex">
        <!-- Utilisez une boucle v-for pour afficher les données de prévisions horaires -->
        <AffichageHeure
          v-for="(data, index) in hourlyForecastData"
          :key="index"
          :heure="data.time"
          :imgMeteo="data.weather_description"
          :temperature="data.temperature"
          :pourcentagePluie="data.precipitation_proba"
          :vitesseVent="data.wind_speed"
        />
      </div>
    </div>

      <div class="flex justify-between m-4">
        <button
          @click="precedent()"
          class="pl-5 pr-5 py-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full mr-2"
        >
          Précédent
        </button>
        <button
          @click="suivant()"
          class="pl-5 pr-5 py-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ml-2"
        >
          Suivant
        </button>
      </div>

      <!-- Bouton pour revenir à l'accueil -->
      <nuxt-link
        :to="`/universities/${selectedCampus}`"
        class="pl-20 pr-20 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out"
      >
        Retour à l'accueil
      </nuxt-link>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import AffichageHeure from "~/components/AffichageHeure.vue";
import { get_hourly_forecast } from "@/api/weatherApi"; // Importez la fonction pour récupérer les données

const route = useRoute();
const selectedCampus = route.params.campus;

let hourlyForecastData = []; // Variable pour stocker les données de prévisions horaires

// Fonction pour récupérer les données de l'API
const fetchDataFromApi = async () => {
  try {
    // Récupérez les données de prévisions horaires
    hourlyForecastData = await get_hourly_forecast(lat, lon, api_key);
    console.log("Data fetched successfully");
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

// Appelez la fonction pour récupérer les données lors de l'initialisation du composant
onMounted(fetchDataFromApi);


const initialiserFenetreAffichage = () => {
  isMobile.value = window.innerWidth < 768;
  const nbHeuresAffichees = isMobile.value ? 4 : 8; // 4 pour mobile, 8 pour PC
  fenetreAffichage.value = Array.from({ length: nbHeuresAffichees }, (_, i) => i);
};

const ajusterFenetreAffichage = () => {
  initialiserFenetreAffichage();
};

const precedent = () => {
  if (fenetreAffichage.value[0] > 0) {
    fenetreAffichage.value = fenetreAffichage.value.map((indice) => indice - 1);
  }
};

const suivant = () => {
  if (
    fenetreAffichage.value[fenetreAffichage.value.length - 1] <
    affichageheure.length - 1
  ) {
    fenetreAffichage.value = fenetreAffichage.value.map((indice) => indice + 1);
  }
};



onMounted(() => {
  initialiserFenetreAffichage();
  window.addEventListener("resize", ajusterFenetreAffichage);
});
onBeforeUnmount(() => {
  window.removeEventListener("resize", ajusterFenetreAffichage);
});
</script>
