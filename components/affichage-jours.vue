<template>
  <div>
    <div
      :class="[
        'container',
        { 'md:w-1/4': !isMobile }
      ]"
    >
      <div
        class="bg-gradient-to-b from-blue-400 to-blue-300 w-20 h-40 rounded-3xl flex flex-col items-center justify-center mt-4 mb-4 ml-2 mr-2 shadow-lg"
      >
        <div
          class="text-black text_xs text-center flex flex-col items-center justify-center"
        >
          <!-- Affichage du jour de la semaine -->
          <h1 class="text-xs text-white mt-2">{{ jourSemaine }}</h1>
          <img
            src="~/../assets/images/neige.png/"
            alt=""
            class="w-10 h-10 mt-2"
          />
          <p class="text-xs text-white m-2">{{ temperature }}°C</p>
          <p class="text-xs text-white m-2">{{ min }}°C / {{ max }}°C</p>
          <p class="text-xs text-white m-2">{{ vitesseVent }} km/h</p>
          <img src="~/../assets/images/vent.png" alt="" class="w-4 h-4 mr-1" />
          <p class="text-xs text-white m-2">Vitesse du vent</p>
        </div>
        <div class="hidden md:flex flex-row items-center justify-center m-1">
          
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, computed } from "vue";

const props = defineProps({
  date: String,  // Assurez-vous que vous passez 'date' comme prop dans le composant parent
  min: Number,
  max: Number,
  temperature: Number,
  vitesseVent: Number,
});

const isMobile = computed(() => {
  return window.innerWidth < 768;
});

// Convertir la date en nom de jour
const jourSemaine = computed(() => {
  const jours = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'];
  const dateObj = new Date(props.date);
  return jours[dateObj.getDay()];
});
</script>
