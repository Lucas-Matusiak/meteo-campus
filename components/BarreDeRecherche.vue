<template>
  <div>
    <input
      type="text"
      v-model="input"
      placeholder="Recherchez un campus..."
      class="block w-64 mt-6 px-4 py-2 rounded bg-white bg-no-repeat bg-right border border-gray-300 focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
    />
    <div v-if="filteredList().length > 0" class="grid grid-cols-1 gap-4 mt-4">
      <div
        v-for="campus in filteredList()"
        :key="campus"
        class="bg-blue-500 text-white rounded p-4"
      >
        <p @click="updateInput(campus)">{{ campus }}</p>
        <!-- Ajout du gestionnaire d'événements @click -->
      </div>
    </div>
    <div v-else class="bg-red-500 text-white rounded p-4 mt-4">
      <p>No results found!</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
let input = ref("");
const fruits = ["apple", "banana", "orange"];
function filteredList() {
  return fruits.filter((fruit) =>
    fruit.toLowerCase().includes(input.value.toLowerCase())
  );
}

function updateInput(value) {
  input.value = value; // Met à jour la valeur de l'input avec celle du campus
}
</script>

<style scoped></style>
