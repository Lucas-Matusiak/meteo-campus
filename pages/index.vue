<template>
  <div class="m-3 flex justify-center items-center flex-col">
    <RechercheCampus class="m-8" @selected-campus="setCampus($event)" />
    <NuxtLink
      v-if="selectedCampus"
      :to="`/meteo/${selectedCampus}`"
      class="px-6 py-3  bg-opacity-20 bg-indigo-900 backdrop-blur-xl border-opacity-30 rounded-lg hover:bg-[#8BC5D6] transition duration-300 ease-in-out"
    >
      Voir les infos météo
    </NuxtLink>
  </div>
</template>

<script setup>
import RechercheCampus from "~/components/recherche-campus.vue";
const selectedCampus = ref(null);

const setCampus = (value) => {
  selectedCampus.value = value;
};
</script>
