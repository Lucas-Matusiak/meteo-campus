
<template>
  <div class="h-auto flex flex-col justify-center items-center">
    <h1 class="text-3xl font-bold text-center mb-4">Météo Campus</h1>
    <div class=" "> <!-- Météo  -->
      <p> {{ route.params.campus }}</p>
      <div>
        <Temperature/>
        <weather/>
      </div>
      <div>
          
      </div>
      <div>
        <HumiditeVitesseDuVent/>
      </div>
      <div>
        <Soleil/>
      </div>

    <!-- Bouton pour revenir à l'accueil -->
      <nuxt-link :to="`/universities/${selectedCampus}`" class="pl-20 pr-20 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out">
        Retour à l'accueil
      </nuxt-link>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';


const route = useRoute();
const selectedCampus = route.params.campus;

</script>