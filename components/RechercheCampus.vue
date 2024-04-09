<template>
  <div id="chooseUniversity">
    <h1 class="m-5 text-2xl font-bold text-center">Choisis ton université</h1>
    <div class="m-5">
      <input
        type="text"
        v-model="selectedUniversity"
        placeholder="Recherchez une université..."
        @click="handleClickInputUniversity"
        @change="handleChangeInputUniversity"
        class="block w-64 mt-6 px-4 py-2 rounded bg-white bg-no-repeat bg-right border border-gray-300 focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
      />
      <div v-if="displayListUniversity">
        <div
          v-if="filteredList(listUniversities, selectedUniversity).length"
          class="grid grid-cols-1 gap-4 mt-4"
        >
          <div
            v-for="university in filteredList(
              listUniversities,
              selectedUniversity
            )"
            :key="university"
            class="bg-blue-500 text-white rounded p-4"
            @click="updateUniversity(university)"
          >
            <p>{{ university }}</p>
          </div>
        </div>
        <div v-else class="bg-red-500 text-white rounded p-4 mt-4">
          <p>Aucun résultat trouvé</p>
        </div>
      </div>
    </div>
  </div>
  <div id="chooseCampus" v-if="displayCampus">
    <h1 class="m-5 text-2xl font-bold text-center">Choisis ton campus</h1>
    <div class="m-5">
      <input
        type="text"
        placeholder="Recherchez un campus..."
        v-model="selectedCampus"
        @click="handleClickInputCampus"
        @change="displayListCampus = true"
        class="block w-64 mt-6 px-4 py-2 rounded bg-white bg-no-repeat bg-right border border-gray-300 focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
      />
      <div v-if="displayListCampus">
        <div
          v-if="filteredList(listCampus, selectedCampus).length && displayListCampus"
          class="grid grid-cols-1 gap-4 mt-4"
        >
          <div
            v-for="campus in filteredList(listCampus, selectedCampus)"
            :key="campus"
            class="bg-blue-500 text-white rounded p-4"
            @click="updateCampus(campus)"
          >
            <p>{{ campus }}</p>
          </div>
        </div>

        <div v-else class="bg-red-500 text-white rounded p-4 mt-4">
          <p>Aucun résultat trouvé</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from "vue";

// Déclarez les variables réactives
let selectedUniversity = ref("");
let selectedCampus = ref("");
let displayCampus = ref(false);
let displayListUniversity = ref(false);
let displayListCampus = ref(false);

const emit = defineEmits(['selectedCampus'])
// Déclarez les constantes pour les listes d'universités et de campus
const listUniversities = [
  "paris",
  "lyon",
  "bordeaux",
  "bordeaux",
  "bordeaux",
  "bordeaux",
  "bordeaux",
  "bordeaux",
];
const listCampus = [
  "victoire",
  "montaigne",
  "st",
  "st",
  "st",
  "st",
  "st",
  "st",
];

// Définissez la fonction pour filtrer les listes
function filteredList(list, input) {
  return list
    .filter((element) => element.toLowerCase().includes(input.toLowerCase()))
    .slice(0, 5);
}

// Définissez les fonctions pour gérer les interactions utilisateur
function updateUniversity(value) {
  selectedUniversity.value = value;
  displayListUniversity.value = false;
  displayCampus.value = true;
  displayListCampus.value = true;
}
function updateCampus(value) {
  selectedCampus.value = value;
  displayListCampus.value = false;
  emit('selectedCampus', value); // Émettre un événement avec la valeur sélectionnée du campus
}
function handleClickInputUniversity() {
  displayListUniversity.value = true;
}
function handleClickInputCampus() {
  displayListCampus.value = true;
}
function handleChangeInputUniversity() {
  displayListUniversity.value = true;
  displayCampus.value = false;
}
</script>



<style scoped>
/* Vos styles CSS ici */
</style>
