<template>
  <div class="m-5 flex justify-center items-center flex-col">
   <!--  <RechercheCampus @selected-campus="setCampus($event)"/> -->
    <Combobox  class="m-8" @selected-campus="setCampus($event)"/>
    <NuxtLink
      v-if="selectedCampus"
      :to="`/meteo/${selectedCampus}`"
      class="px-6 py-3 bg-blue-500 text-white font-bold rounded-full hover:bg-blue-700 transition duration-300 ease-in-out"
    >
      Voir les infos météo
    </NuxtLink>
    {{ selectedCampus }}
  </div>
</template>

<script setup>

import RechercheCampus from "~/components/RechercheCampus.vue";
import Combobox  from "~/components/Combobox.vue";
const selectedCampus = ref(null);

const setCampus = (value) => {
  console.log(value);
  selectedCampus.value = value;
}
</script>
