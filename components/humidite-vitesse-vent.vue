<template>
  <div class="flex items-center justify-center">
    <div class="pr-10 pt-4 bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-3xl mb-4 shadow-lg mr-4">
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

    <div class="wind-speed pl-4 bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-3xl mb-4 shadow-lg mr-4">
      <div v-if="vitesseVent !== null">
        <img
          src="~/../assets/images/vent.png"
          alt="Logo Vitesse du vent"
          class="logo"
          style="width: 50px; height: auto"
        />
        <h1 class="text-l font-bold bg-clip-text pt-5 text-center">
          {{ vitesseVent }} km/h
        </h1>
        <h1 class="text-1xl bg-clip-text text-center">
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
    humidite: { type: String, default: null },
    vitesseVent: { type: Number, default: null },
  },
};
</script>
