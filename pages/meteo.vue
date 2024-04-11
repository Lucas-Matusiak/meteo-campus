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
    <div class="bg-gradient-to-r from-blue-300 to-indigo-500 rounded-3xl mb-4">
      <h1
        class="text-center text-white font-bold border-b border-white px-4 m-4"
        style="margin-top: 4px; margin-bottom: 4px"
      >
        Prévisions Heure par Heure
      </h1>
      <div class="flex ">
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
    
    <div class="flex justify-between m-4">
  <button @click="precedent()" class="pl-5 pr-5 py-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full mr-2">Précédent </button>
  <button @click="suivant()" class="pl-5 pr-5 py-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ml-2 "> Suivant</button>
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
          heure: "5",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
        {
          heure: "6",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
        {
          heure: "7",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
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
        {
          heure: "12",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
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
        {
          heure: "15",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
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
        {
          heure: "18",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
        {
          heure: "19",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
        {
          heure: "20",
          imgMeteo: "~/../assets/images/lever-soleil.png",
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
        {
          heure: "00",
          temperature: "20",
          pourcentagePluie: "76",
          vitesseVent: "12",
        },
      ],
      fenetreAffichage: [0, 1, 2, 3, 4, 5, 6, 7],
    };
  },
  methods: {
    precedent() {
      if (this.fenetreAffichage[0] > 0) {
        this.fenetreAffichage = this.fenetreAffichage.map(
          (indice) => indice - 1
        );
      }
    },
    suivant() {
      if (this.fenetreAffichage[7] < this.affichageheure.length - 1) {
        this.fenetreAffichage = this.fenetreAffichage.map(
          (indice) => indice + 1
        );
      }
    },
  },
};
</script>