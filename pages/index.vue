<template>
  <div class="m-8 flex justify-center items-center flex-col">
    <BarreDeRecherche  />
    <NuxtLink
      to="/meteo"
      class="px-6 py-3 bg-blue-500 text-white font-bold rounded-full hover:bg-blue-700 transition duration-300 ease-in-out"
    >
      Voir les infos météo
    </NuxtLink>
  </div>
</template>
<script>
import BarreDeRecherche from "~/components/BarreDeRecherche.vue";

export default {
  components: {
    BarreDeRecherche
  },
  // Autres options du composant parent
};
</script>
