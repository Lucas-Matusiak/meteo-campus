<template>
  <div>
    <div :class="[
      'container',
      { 'md:w-1/4 ': !isMobile }, 
    ]">
      <div class="w-40 h-50 rounded-3xl flex flex-col items-center justify-center p-8 mt-4 mb-4 ml-2 mr-2 shadow-lg md:flex bg-opacity-20 bg-indigo-900 backdrop-blur-xl border-opacity-30 rounded-lg shadow-lg text-white">
        <div class="text-black text-center flex flex-col items-center justify-center">

          <h1 class="text-white text-base mt-2 mb-2">{{ heure }}</h1>
          <WeatherIcon :code="code" size="small" />
          <p class="text-xl text-white m-2">{{ temperature }}°</p>

          <!-- Affichage conditionnel pour les écrans larges -->
          <div class="hidden text-base md:flex flex-row items-center justify-center m-2">
            <img src="~/../assets/images/gouttebleue.svg" alt="" class="w-3 h-4 m-2" />
            <p class=" text-white">{{ pourcentagePluie }}%</p>
          </div>
          <div class="hidden md:flex flex-row items-center justify-center m-1">
            <img src="~/../assets/images/ventW.svg" alt="" class="w-4 h-4 m-2" />
            <p class="text-xs text-white text-base">{{ vitesseVent }} km/h</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const isMobile = computed(() => {
  // Vérifie si la largeur de l'écran est inférieure à 768 pixels
  return window.innerWidth < 768;
});

// Props
const props = defineProps({
  heure: String,
  code: String,
  temperature: Number,
  pourcentagePluie: Number,
  vitesseVent: Number,
});
</script>
