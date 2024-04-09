<template>
  <div id="weather">
    <!-- Utilisez v-bind (ou :) pour lier l'attribut src dynamiquement -->
    <img 
      :src= "weather"
      alt="weather"
      class="w-64 h-auto"/>
  </div>
</template>

<script>
export default {
  name: 'weather', // Renommé pour plus de clarté
  data() {
    return {
      weather :'../assets/images/ensoleille.png'
  }
}
}
</script>