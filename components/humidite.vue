<template>
  <div class="flex justify-center">
    <div class="pr-10 pt-4">
      <div v-if="humidite !== null">
        <img
          src="~/../assets/images/Humidite.png"
          alt="Logo Humidité"
          class="logo"
        />
        <h1 class="text-2xl font-bold bg-clip-text pt-5 text-center">
          {{ humidite }}%
        </h1>
        <h1 class="text-1xl font-bold bg-clip-text text-center">Humidité</h1>
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
