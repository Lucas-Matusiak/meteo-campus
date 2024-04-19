<template>
  <div class="flex justify-center">
    <div class="wind-speed pl-4">
      <div v-if="vitesseVent !== null">
        <img
          src="~/../assets/images/vent.svg"
          alt="Logo Vitesse du vent"
          class="logo"
        />
        <h1 class="text-2xl font-bold bg-clip-text pt-5 text-center">
          {{ vitesseVent }} km/h
        </h1>
        <h1 class="text-1xl font-bold bg-clip-text text-center">
          Vitesse du vent
        </h1>
      </div>
    </div>
  </div>
</template>
<script>
// Définition du composant Vue.js
export default {
  // Déclaration des propriétés du composant
  props: {
    vitesseVent: { type: Number, default: null },
  },
};
</script>
