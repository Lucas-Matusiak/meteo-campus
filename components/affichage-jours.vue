<template>
  <div class="container mx-auto">
    <div class="flex flex-col items-center justify-center">
      <!-- Contenu visible sur mobile uniquement -->
      <div
        class="flex flex-row items-center justify-center text-center text-white border-t border-white px-4 mx-1 md:hidden"
      >
        <Weather :code="code" :showText="False" />
        <p class="text-lg px-6">{{ temperature }}°C</p>
        <h1 class="text-sm">{{ jourSemaine }}</h1>
      </div>

      <!-- Contenu visible sur tablette et desktop uniquement -->
      <div
        class="hidden md:flex bg-gradient-to-b from-[#298DAD] to-[#A4D8E8] rounded-3xl flex-col items-center justify-center text-center text-white p-3 mb-4 mt-4"
      >
        <h1 class="text-xs mt-2">{{ jourSemaine }}</h1>
        <Weather :code="code" :showText="False" />
        <p class="text-xs m-2">{{ temperature }}°C</p>
        <p class="text-xs m-2">{{ min }}°C / {{ max }}°C</p>
        <p class="text-xs m-2">{{ vitesseVent }} km/h</p>
        <img
          src="~/../assets/images/vent.svg"
          alt="Vent"
          class="w-4 h-4 mr-1"
        />
        <p class="text-xs m-2">Vitesse du vent</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import Weather from "./weather.vue";

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
