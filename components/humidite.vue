<template>
  <div class="flex items-center justify-center">
    <div class="flex flex-col items-center justify-center bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-lg shadow-md w-full max-w-md mx-auto p-4 md:p-6 mr-6 mb-4">
      <div v-if="humidite !== null">
        <img
          src="~/../assets/images/Humidite.png"
          alt="Logo Humidité"
          class="logo"
          style="width: 50px; height: auto"
        />
        <h1 class="text-l font-bold bg-clip-text pt-5 text-center">
          {{ humidite }}%
        </h1>
        <h1 class="text-1xl bg-clip-text text-center">Humidité</h1>
      </div>
    </div>

   
  </div>
</template>
<script>
// Définition du composant Vue.js
export default {
  // Déclaration des propriétés du composant
  props: {
    humidite: { type: String, default: null },
  },
};
</script>
