<template>
  <div class="mb-10">
    <!-- Affichage conditionnel des images et descriptions basé sur le code météo -->
    <div v-if="code.toString().startsWith('2')"  class="flex">
      <img
        src="../assets/images/Orage.svg"
        class="content-center object-scale-down h-12 w-auto mx-5"
      />
      <h1 v-if="showText" class="text-1xl text-center self-center">Orageux</h1>
    </div>
    <div v-else-if="code.toString().startsWith('3')" class="flex">
      <img
        src="../assets/images/bruineux.svg"
        class="content-center object-scale-down h-12 w-auto mx-5"
      />
      <h1 v-if="showText" class="text-1xl text-center self-center">Bruineux</h1>
    </div>
    <div v-else-if="code.toString().startsWith('5')" class="flex">
      <img
        src="../assets/images/Pluie.svg"
        class="content-center object-scale-down h-12 w-auto mx-5"
      />
      <h1 v-if="showText" class="text-1xl text-center self-center">Pluvieux</h1>
    </div>
    <div v-else-if="code.toString().startsWith('6')" class="flex">
      <img
        src="../assets/images/Neige.svg"
        class="content-center object-scale-down h-12 w-auto mx-5"
      />
      <h1 v-if="showText" class="text-1xl text-center self-center">Neigeux</h1>
    </div>
    <div v-else-if="code.toString().startsWith('7')" class="flex">
      <img
        src="../assets/images/evente.svg"
        class="content-center object-scale-down h-12 w-auto mx-5"
      />
      <h1 v-if="showText" class="text-1xl text-center self-center">Eventé</h1>
    </div>
    <div v-if="code.toString().startsWith('8') && code !== 800" class="flex">
      <img
        src="../assets/images/nuage.svg"
        class="content-center object-scale-down h-12 w-auto mx-5"
      />
      <h1  v-if="showText" class="text-1xl text-center self-center">Nuageux</h1>
    </div>
    <div v-else-if="code == 800" class="flex">
      <img
        src="../assets/images/ensoleille.svg"
        class="content-center object-scale-down h-12 w-auto mx-5"
      />
      <h1 v-if="showText" class="text-1xl text-center self-center">Ensoleillé</h1>
    </div>
    <!-- Ajoutez plus de conditions ici selon les groupes de codes météo -->
  </div>
</template>

<script setup>
  import { defineProps } from 'vue';

  const props = defineProps({
    code: { type: String, default: null },
    showText: { type: Boolean, default: true } // Nouvelle prop pour afficher ou non le texte
  });
</script>
