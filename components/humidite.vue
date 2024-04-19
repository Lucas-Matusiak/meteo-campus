<template>
  <div v-if="humidite !== null">
    <div class="flex flex-col items-center">
      <img
        src="~/../assets/images/Humidite.svg"
        alt="Logo Humidité"
        class="logo"
        style="width: 50px; height: 49.58px"
      />
      <h1 class="text-l font-bold bg-clip-text pt-5 text-center">{{ humidite }}%</h1>
      <h1 class="text-1xl bg-clip-text text-center">Humidité</h1>
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
