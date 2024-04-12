<template>
  <div class="m-8 flex justify-center items-center flex-col">
    <RechercheCampus @selected-campus="setCampus($event)" :data="route.params.university"/>
    <NuxtLink
      :to="`/meteo/${selectedCampus}`"
      class="px-6 py-3 bg-blue-500 text-white font-bold rounded-full hover:bg-blue-700 transition duration-300 ease-in-out"
    >
      Voir les infos météo
    </NuxtLink>
  </div>
</template>

<script setup>
import RechercheCampus from "~/components/RechercheCampus.vue";
import { useRoute } from 'vue-router';

const route = useRoute();
const selectedCampus = ref(null);

const setCampus = (value) => {
  selectedCampus.value = value;
}

</script>
