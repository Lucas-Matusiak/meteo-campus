<template>
  <div>
    <div :class="[
      'container',
      { 'md:w-1/4': !isMobile }, 
    ]">
      <div :class="{
      'bg-gradient-to-b from-blue-900 to-slate-500':
        heure >= 0 && heure < 5, // Nuit
      'bg-gradient-to-b from-blue-300 to-indigo-500':
        heure >= 5 && heure < 7, // Lever du soleil
      'bg-gradient-to-t from-blue-300 to-indigo-500':
        heure >= 7 && heure < 11, // Matin
      'bg-gradient-to-b from-blue-400 to-blue-300':
        heure >= 11 && heure < 17, // Journée
      'bg-gradient-to-b from-blue-300 to-indigo-500':
        heure >= 17 && heure < 20, // Soirée
      'bg-gradient-to-b from-indigo-500 to-blue-900':
        heure >= 20 && heure < 24, // Nuit
    }" class="w-20 h-40 rounded-3xl flex flex-col items-center justify-center mt-4 mb-4 ml-2 mr-2 shadow-lg">
        <div class="text-black text_xs text-center flex flex-col items-center justify-center">

          <h1 class="text_xs text-white mt-2">{{ heure }}</h1>
          <WeatherIcon :code="code" size="small" />
          <p class="text-xs text-white m-2">{{ temperature }}°</p>

          <!-- Affichage conditionnel pour les écrans larges -->
          <div class="hidden md:flex flex-row items-center justify-center m-1">
            <img src="~/../assets/images/gouttebleue.svg" alt="" class="w-3 h-4 mr-1" />
            <p class="text-xs">{{ pourcentagePluie }}%</p>
          </div>
          <div class="hidden md:flex flex-row items-center justify-center m-1">
            <img src="~/../assets/images/vent.svg" alt="" class="w-4 h-4 mr-1" />
            <p class="text-xs">{{ vitesseVent }} km/h</p>
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
