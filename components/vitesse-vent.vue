<template>
  <div v-if="vitesseVent !== null">
    <div class="flex flex-col items-center">
        <img
          src="~/../assets/images/ventW.svg"
          alt="Logo Vitesse du vent"
          class="logo"
          style="width: 50px; height: auto"
        />
        <h1 class="text-l font-bold bg-clip-text pt-5 text-center">
          {{ vitesseVent }} km/h
        </h1>
        <h1 class="text-1xl bg-clip-text text-center">Vitesse du vent</h1>
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