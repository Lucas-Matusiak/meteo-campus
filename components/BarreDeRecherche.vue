<template>
  <div id="chooseUniversity">
    <h1 class="m-5 text-2xl font-bold">Choisis ton université</h1>
    <div class="m-5">
      <input
        type="text"
        v-model="input"
        placeholder="Recherchez un campus..."
        @click="displayCampus=false"
        class="block w-64 mt-6 px-4 py-2 rounded bg-white bg-no-repeat bg-right border border-gray-300 focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
      />
      <div v-if="input && !displayCampus">
        <div v-if="filteredList().length" class="grid grid-cols-1 gap-4 mt-4">
          <div
            v-for="university in filteredList()"
            :key="university"
            class="bg-blue-500 text-white rounded p-4"
            @click="updateInput(university)"
          >
            <p>{{ university }}</p>
            <!-- Ajout du gestionnaire d'événements @click -->
          </div>
        </div>
        <div v-else class="bg-red-500 text-white rounded p-4 mt-4">
          <p>Aucun résultat trouvé</p>
        </div>
      </div>
    </div>
  </div>
  <div id="chooseCampus" v-if="displayCampus">
    <h1 class="m-5 text-2xl font-bold">Choisis ton campus</h1>
  </div>
</template>

<script setup>
import { ref } from "vue";
let input = ref("");
let displayCampus = false;
const listUniversities = [
  "apple",
  "banana",
  "orange",
  "orange",
  "orange",
  "orange",
  "orange",
  "orange",
];
function filteredList() {
  return listUniversities
    .filter((university) => university.toLowerCase().includes(input.value.toLowerCase()))
    .slice(0, 5);
}

function updateInput(value) {
  input.value = value; // Met à jour la valeur de l'input avec celle du campus
  this.displayCampus = true;
}
</script>

<style scoped></style>
