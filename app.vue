<template>
  <div class="m-8 flex justify-center items-center flex-col">
    <h1 class="m-5 text-2xl font-bold">Choisis ton campus</h1>
    <BarreDeRecherche />
  </div>
</template>
<script>
import BarreDeRecherche from "~/components/BarreDeRecherche.vue";

export default {
  components: {
    BarreDeRecherche,
  },
  // Autres options du composant parent
};
</script>
<style scoped></style>
