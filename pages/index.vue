<template>
  <div class="m-8 flex justify-center items-center flex-col">
    <RechercheCampus @selected-campus="myCampus"/>
    <NuxtLink
      to="/meteo"
      class="px-6 py-3 bg-blue-500 text-white font-bold rounded-full hover:bg-blue-700 transition duration-300 ease-in-out"
    >
      Voir les infos météo
    </NuxtLink>
  </div>
</template>

<script>
import RechercheCampus from "~/components/RechercheCampus.vue";

export default {
  components: {
    RechercheCampus
  },
  data() {
    return {
      selectedCampus: "00" // Définir la valeur initiale de selectedCampus
    };
  },

  methods:{
    myCampus(value){
      this.selectedCampus=value;
    }
  }
};
</script>
