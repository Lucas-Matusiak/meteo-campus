<template>
  <div>
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
            v-if="
              filteredList(listCampus, selectedCampus).length &&
              displayListCampus
            "
            class="grid grid-cols-1 gap-4 mt-4"
          >
            <div
              v-for="campus in filteredList(listCampus, selectedCampus)"
              :key="campus"
              class="bg-blue-500 text-white rounded p-4"
              @click="updateCampus(campus)"
            >
              <p>{{ campus }}</p>
              <!-- Ajout du gestionnaire d'événements @click -->
            </div>
          </div>

          <div v-else class="bg-red-500 text-white rounded p-4 mt-4">
            <p>Aucun résultat trouvé</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const selectedUniversity = ref("");
const selectedCampus = ref("");
const displayCampus = ref(false);
const displayListUniversity = ref(false);
const displayListCampus = ref(false);
const listUniversities = ref([]);
const listCampus = ref([]);

const handleClickInputUniversity = () => {
  displayListUniversity.value = true;
};

const handleClickInputCampus = () => {
  displayListCampus.value = true;
};

const handleChangeInputUniversity = () => {
  displayListUniversity.value = true;
  displayCampus.value = false;
};

const updateUniversity = async (university) => {
  selectedUniversity.value = university;
  displayListUniversity.value = false;
  displayCampus.value = true;
  displayListCampus.value = true;
  await fetchCampuses(university);
};

const updateCampus = (campus) => {
  selectedCampus.value = campus;
  displayListCampus.value = false;
};

const filteredList = (list, input) => {
  return list
    .filter((element) => element.toLowerCase().includes(input.toLowerCase()))
    .slice(0, 5);
};

// Function to fetch universities from API
const fetchUniversities = async () => {
  try {
    const response = await axios.get("http://localhost:8080/api/universities");
    listUniversities.value = response.data.map(
      (university) => university.etablissement_siege
    );
  } catch (error) {
    console.error("Error fetching universities:", error);
  }
};

// Function to fetch campuses based on selected university
const fetchCampuses = async (university) => {
  try {
    console.log("Fetching campus ....");
    const response = await axios.get(
      `http://localhost:8080/api/implantations?etablissement_siege=\"${university}\"`
    );
    console.log(response);
    listCampus.value = response.data.map((campus) => campus.nom_implantation);
    console.log(listCampus);
  } catch (error) {
    console.error("Error fetching campuses:", error);
  }
};

// Call fetchUniversities when component is mounted
fetchUniversities();
</script>

<style scoped></style>
