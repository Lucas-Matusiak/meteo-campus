<template>
  <div class="container">
    <img src="assets\images\logo.png" alt="Description de l'image" class="image-top-left">
    <NuxtWelcome />
  </div>
</template>

<template>
  <div>
    <h1 class="text-3xl font-bold underline">Hello world !</h1>
    <BarreDeRecherche />
  </div>
</template>

<style scoped>
.container {
  position: relative;
}

.image-top-left {
  position: absolute;
  top: 10px; /* Ajustez selon votre besoin */
  left: 10px; /* Ajustez selon votre besoin */
  width: 100px; /* Ajustez selon la taille de votre image */
  height: auto; /* Ajustez selon la taille de votre image */
}


</style>

<script>
import BarreDeRecherche from '~/components/BarreDeRecherche.vue'

export default {
  components: {
    BarreDeRecherche
  }
  // Autres options du composant parent
}
</script>