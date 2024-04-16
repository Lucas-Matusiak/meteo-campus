<template>
  <div>
    <div id="chooseUniversity" class="w-72">
      <h1 class="m-5 text-2xl font-bold text-center">Choisis ton université</h1>
      <Combobox v-model="selectedUniversity" @change="updateCampus()">
        <div class="relative mt-1">
          <div
            class="relative w-full cursor-default overflow-hidden rounded-lg bg-white text-left shadow-md focus:outline-none focus-visible:ring-2 focus-visible:ring-white/75 focus-visible:ring-offset-2 focus-visible:ring-offset-teal-300 sm:text-sm"
          >
            <ComboboxInput
              class="w-full border-none py-2 pl-3 pr-10 text-sm leading-5 text-gray-900 focus:ring-0"
              :displayValue="(selectedUniversity) => selectedUniversity"
              @change="handleChangeInputUniversity($event)"
              placeholder="Recherchez une université..."
            />
            <ComboboxButton
              class="absolute inset-y-0 right-0 flex items-center pr-2"
            >
              <ChevronUpDownIcon
                class="h-5 w-5 text-gray-400"
                aria-hidden="true"
              />
            </ComboboxButton>
          </div>
          <TransitionRoot
            leave="transition ease-in duration-100"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
            @after-leave="queryUniversity = ''"
          >
            <ComboboxOptions
              class="absolute mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black/5 focus:outline-none sm:text-sm z-50"
            >
              <div
                v-if="!filteredList(listUniversities, queryUniversity).length"
                class="relative cursor-default select-none px-4 py-2 text-gray-700"
              >
                Nothing found.
              </div>
              <ComboboxOption
                v-for="university in filteredList(
                  listUniversities,
                  queryUniversity
                )"
                as="template"
                :key="university"
                :value="university"
                v-slot="{ selected, active }"
                @click="updateUniversity()"
              >
                <li
                  class="relative cursor-default select-none py-2 pl-10 pr-4"
                  :class="{
                    'bg-teal-600 text-white': active,
                    'text-gray-900': !active,
                  }"
                >
                  <span
                    class="block"
                    :class="{
                      'font-medium': selectedUniversity,
                      'font-normal': !selectedUniversity,
                    }"
                  >
                    {{ university }}
                  </span>
                  <span
                    v-if="selected"
                    class="absolute inset-y-0 left-0 flex items-center pl-3"
                    :class="{ 'text-white': active, 'text-teal-600': !active }"
                  >
                    <CheckIcon class="h-5 w-5" aria-hidden="true" />
                  </span>
                </li>
              </ComboboxOption>
            </ComboboxOptions>
          </TransitionRoot>
        </div>
      </Combobox>
    </div>
    <div id="chooseCampus" class="w-72" v-if="selectedUniversity">
      <h1 class="m-5 text-2xl font-bold text-center">Choisis ton campus</h1>
      <Combobox v-model="selectedCampus" @update="updateCampus()">
        <div class="relative mt-1">
          <div
            class="relative w-full cursor-default overflow-hidden rounded-lg bg-white text-left shadow-md focus:outline-none focus-visible:ring-2 focus-visible:ring-white/75 focus-visible:ring-offset-2 focus-visible:ring-offset-teal-300 sm:text-sm"
          >
            <ComboboxInput
              class="w-full border-none py-2 pl-3 pr-10 text-sm leading-5 text-gray-900 focus:ring-0"
              :displayValue="(selectedCampus) => selectedCampus"
              @change="handleChangeInputCampus($event)"
              placeholder="Recherchez une université..."
            />
            <ComboboxButton
              class="absolute inset-y-0 right-0 flex items-center pr-2"
            >
              <ChevronUpDownIcon
                class="h-5 w-5 text-gray-400"
                aria-hidden="true"
              />
            </ComboboxButton>
          </div>
          <TransitionRoot
            leave="transition ease-in duration-100"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
            @after-leave="queryCampus = ''"
          >
            <ComboboxOptions
              class="absolute mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black/5 focus:outline-none sm:text-sm"
            >
              <div
                v-if="!filteredList(listCampus, queryCampus).length"
                class="relative cursor-default select-none px-4 py-2 text-gray-700"
              >
                Nothing found.
              </div>
              <ComboboxOption
                v-for="campus in filteredList(listCampus, queryCampus)"
                as="template"
                :key="campus"
                :value="campus"
                v-slot="{ selected, active }"
                @click="updateCampus()"
              >
                <li
                  class="relative cursor-default select-none py-2 pl-10 pr-4"
                  :class="{
                    'bg-teal-600 text-white': active,
                    'text-gray-900': !active,
                  }"
                >
                  <span
                    class="block"
                    :class="{
                      'font-medium': selectedCampus,
                      'font-normal': !selectedCampus,
                    }"
                  >
                    {{ campus }}
                  </span>
                  <span
                    v-if="selected"
                    class="absolute inset-y-0 left-0 flex items-center pl-3"
                    :class="{ 'text-white': active, 'text-teal-600': !active }"
                  >
                    <CheckIcon class="h-5 w-5" aria-hidden="true" />
                  </span>
                </li>
              </ComboboxOption>
            </ComboboxOptions>
          </TransitionRoot>
        </div>
      </Combobox>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue";
import axios from "axios";

import {
  Combobox,
  ComboboxInput,
  ComboboxButton,
  ComboboxOptions,
  ComboboxOption,
  TransitionRoot,
} from "@headlessui/vue";
import { CheckIcon, ChevronUpDownIcon } from "@heroicons/vue/20/solid";

const props = defineProps(["campus", "university"]);
const old_campus = props.campus;
const old_university = props.university;

let selectedUniversity = ref("");
let selectedCampus = ref("");

const emit = defineEmits(["selectedCampus"], ["selectedUniversity"]);
let listUniversities = ref([]);
let listCampus = ref([]);
let queryUniversity = ref("");
let queryCampus = ref("");

function filteredList(list, input) {
  return list.filter((element) =>
    element
      .toLowerCase()
      .replace(/\s+/g, "")
      .includes(input.toLowerCase().replace(/\s+/g, ""))
  );
}

function handleChangeInputUniversity(event) {
  queryUniversity.value = event.target.value;
}
function handleChangeInputCampus(event) {
  queryCampus.value = event.target.value;
}
async function updateUniversity() {
  //selectedCampus.value = "";
  await fetchCampuses(selectedUniversity.value);
  updateCampus();
}
const updateCampus = () => {
  emit("selectedCampus", selectedCampus.value);
  emit("selectedUniversity", selectedUniversity.value);
};

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

if (old_campus && old_university) {
  console.log(old_campus);
  selectedCampus.value = old_campus;
  selectedUniversity.value = old_university;
  fetchUniversities();
  fetchCampuses(selectedUniversity.value);
  updateCampus();
} else {
  fetchUniversities();
}
</script>
