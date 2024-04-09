<template>
  <div class="h-auto flex flex-col justify-center items-center">
    <h1 class="text-4xl font-bold text-center mb-4">Prévisions météo</h1>
    <div class="flex flex-wrap justify-center">
      <!-- Météo  -->
      <div>
        <Temperature />
        <weather />
      </div>
      <div></div>
      <div>
        <HumuditeVitesseDuVent />
      </div>
      <div>
        <Soleil />
      </div>
    </div>
    <div class="overflow-x-auto max-w-full">
      <div class="flex">
        <AffichageHeure
          v-for="(heure, index) in affichageheure"
          :key="index"
          :heure="heure.heure"
          :temperature="heure.temperature"
          :pourcentagePluie="heure.pourcentagePluie"
          :vitesseVent="heure.vitesseVent"
        />
      </div>
    </div>
    <!-- Bouton pour revenir à l'accueil -->
    <nuxt-link
      to="/"
      class="pl-20 pr-20 py-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out"
    >
      Retour à l'accueil
    </nuxt-link>
  </div>
</template>

<script>
import AffichageHeure from "~/components/AffichageHeure.vue";

export default {
  components: {
    AffichageHeure,
  },

  data() {
    return {
      affichageheure: [
        {
          heure: "6",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
        {
          heure: "9",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
        {
          heure: "12",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
        {
          heure: "15",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
        {
          heure: "18",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
        {
          heure: "21",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
        {
          heure: "0",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
        {
          heure: "12",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
        {
          heure: "12",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
      ],
    };
  },
};
</script>
