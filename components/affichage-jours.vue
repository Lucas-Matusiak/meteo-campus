<template>
  <div class="container mx-auto">
    <div class="flex flex-col items-center justify-center">
      <!-- Contenu visible sur mobile uniquement -->
      <div
        class="flex flex-row items-center justify-center text-center text-white border-t border-white px-4 mx-1 md:hidden"
      >
        <WeatherIcon :code="code" :showText=false />
        <p class="text-lg px-6">{{ temperature }}°C</p>
        <h1 class="text-sm">{{ jourSemaine }}</h1>
      </div>

      <!-- Contenu visible sur tablette et desktop uniquement -->
      <div
        class="hidden md:flex bg-gradient-to-b from-[#298DAD] to-[#54aec9] rounded-3xl flex-col items-center justify-center text-center text-white p-6 mb-4 mt-4"
      >
        <h1 class="text-xs mt-2 mb-2">{{ jourSemaine }}</h1>
        <WeatherIcon :code="code" size="small" />
        <p class="text-xs m-2">{{ temperature }}°C</p>
        <p class="text-xs m-2">{{ min }}°C / {{ max }}°C</p>
        <div class="hidden md:flex flex-row items-center justify-center m-1">
            <img src="~/../assets/images/ventW.svg" alt="" class="w-4 h-4 mr-1" />
            <p class="text-xs">{{ vitesseVent }} km/h</p>
          </div>
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
  code: String,
});
// On utilise directement les classes de Tailwind pour la réactivité donc pas besoin de computed isMobile.
const jourSemaine = computed(() => {
  const jours = [
    "Dimanche",
    "Lundi",
    "Mardi",
    "Mercredi",
    "Jeudi",
    "Vendredi",
    "Samedi",
  ];
  const dateObj = new Date(props.date);
  return jours[dateObj.getDay()];
});
</script>
