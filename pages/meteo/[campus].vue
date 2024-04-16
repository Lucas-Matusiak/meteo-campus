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
      <div v-if="weatherData && weatherData.current_weather && weatherData.current_weather.code">
        <weather :code="weatherData.current_weather.code"/>
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
        <div class="flex">
          <AffichageHeure
            v-for="indice in fenetreAffichage"
            :key="indice"
            :heure="affichageheure[indice].heure"
            :imgMeteo="affichageheure[indice].imgMeteo"
            :temperature="affichageheure[indice].temperature"
            :pourcentagePluie="affichageheure[indice].pourcentagePluie"
            :vitesseVent="affichageheure[indice].vitesseVent"
          />
        </div>
      </div>

      <div class="flex justify-between m-4 py-3">
        <button
          @click="precedent()"
          class="pl-5 pr-5  bg-[#469FBB] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full mr-2"
        >
          Précédent
        </button>
        <button
          @click="suivant()"
          class="pl-5 pr-5  bg-[#469FBB] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ml-2"
        >
          Suivant
        </button>
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
import Temperature from "~/components/temperature.vue"; // Import du composant Temperature.vue
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

const isMobile = ref(true);
let fenetreAffichage = ref([]);

const affichageheure = [
  { heure: "5", temperature: "20", pourcentagePluie: "76", vitesseVent: "12" },
  { heure: "6", temperature: "20", pourcentagePluie: "76", vitesseVent: "12" },
  { heure: "7", temperature: "20", pourcentagePluie: "76", vitesseVent: "12" },
  {
    heure: "8",
    imgMeteo: "~/../assets/images/lever-soleil.png",
    temperature: "20",
    pourcentagePluie: "76",
    vitesseVent: "12",
  },
  {
    heure: "9",
    imgMeteo: "~/../assets/images/lever-soleil.png",
    temperature: "20",
    pourcentagePluie: "76",
    vitesseVent: "12",
  },
  {
    heure: "10",
    imgMeteo: "~/../assets/images/lever-soleil.png",
    temperature: "20",
    pourcentagePluie: "76",
    vitesseVent: "12",
  },
  {
    heure: "11",
    imgMeteo: "~/../assets/images/lever-soleil.png",
    temperature: "20",
    pourcentagePluie: "76",
    vitesseVent: "12",
  },
  { heure: "12", temperature: "20", pourcentagePluie: "76", vitesseVent: "12" },
  {
    heure: "13",
    imgMeteo: "~/../assets/images/lever-soleil.png",
    temperature: "20",
    pourcentagePluie: "76",
    vitesseVent: "12",
  },
  {
    heure: "14",
    imgMeteo: "~/../assets/images/lever-soleil.png",
    temperature: "20",
    pourcentagePluie: "76",
    vitesseVent: "12",
  },
  { heure: "15", temperature: "20", pourcentagePluie: "76", vitesseVent: "12" },
  {
    heure: "16",
    imgMeteo: "~/../assets/images/lever-soleil.png",
    temperature: "20",
    pourcentagePluie: "76",
    vitesseVent: "12",
  },
  {
    heure: "17",
    imgMeteo: "~/../assets/images/lever-soleil.png",
    temperature: "20",
    pourcentagePluie: "76",
    vitesseVent: "12",
  },
  { heure: "18", temperature: "20", pourcentagePluie: "76", vitesseVent: "12" },
  { heure: "19", temperature: "20", pourcentagePluie: "76", vitesseVent: "12" },
  {
    heure: "20",
    imgMeteo: "~/../assets/images/lever-soleil.png",
    temperature: "20",
    pourcentagePluie: "76",
    vitesseVent: "12",
  },
  { heure: "21", temperature: "20", pourcentagePluie: "76", vitesseVent: "12" },
  {
    heure: "22",
    imgMeteo: "~/../assets/images/lever-soleil.png",
    temperature: "20",
    pourcentagePluie: "76",
    vitesseVent: "12",
  },
  {
    heure: "23",
    imgMeteo: "~/../assets/images/lever-soleil.png",
    temperature: "20",
    pourcentagePluie: "76",
    vitesseVent: "12",
  },
  { heure: "00", temperature: "20", pourcentagePluie: "76", vitesseVent: "12" },
];

const initialiserFenetreAffichage = () => {
  isMobile.value = window.innerWidth < 768;
  const nbHeuresAffichees = isMobile.value ? 4 : 8; // 4 pour mobile, 8 pour PC
  fenetreAffichage.value = Array.from(
    { length: nbHeuresAffichees },
    (_, i) => i
  );
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
