<template>
  <div class="container mx-auto p-4">
    <div class="bg-gradient-to-b from-blue-400 to-blue-300 rounded-3xl flex flex-col items-center justify-center shadow-lg m-2">
      <!-- Contenu visible sur mobile uniquement -->
      <div class="flex flex-col items-center justify-center text-center text-white p-4 md:hidden">
        <img
          src="~/../assets/images/neige.png"
          alt="Neige"
          class="w-14 h-14 mb-2"
        />
        <p class="text-lg">{{ temperature }}°C</p>
        <h1 class="text-sm">{{ jourSemaine }}</h1>
      </div>

      <!-- Contenu visible sur tablette et desktop uniquement -->
      <div class="hidden md:flex flex-col items-center justify-center text-center text-white p-4">
        <h1 class="text-xs mt-2">{{ jourSemaine }}</h1>
        <img
          src="~/../assets/images/neige.png"
          alt="Neige"
          class="w-10 h-10 mt-2"
        />
        <p class="text-xs m-2">{{ temperature }}°C</p>
        <p class="text-xs m-2">{{ min }}°C / {{ max }}°C</p>
        <p class="text-xs m-2">{{ vitesseVent }} km/h</p>
        <img src="~/../assets/images/vent.png" alt="Vent" class="w-4 h-4 mr-1" />
        <p class="text-xs m-2">Vitesse du vent</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const props = defineProps({
  date: String,
  min: Number,
  max: Number,
  temperature: Number,
  vitesseVent: Number,
});

// On utilise directement les classes de Tailwind pour la réactivité donc pas besoin de computed isMobile.
const jourSemaine = computed(() => {
  const jours = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'];
  const dateObj = new Date(props.date);
  return jours[dateObj.getDay()];
});
</script>
