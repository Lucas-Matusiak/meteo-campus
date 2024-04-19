<template>
  <h1 class="text-1xl font-bold text-center">StylAI</h1>

  <div class="flex justify-center">
    <!-- Bloc pour l'accessoire -->
    <div
      v-if="accessoireprediction !== null"
      class="flex items-center pr-1 pt-4 "
    >
      <div class="flex flex-col items-center ">
        <img
          src="~/../assets/images/Accessoire1.svg"
          alt="Logo Accessoire"
          class="w-20 h-auto mb-2"
        />
        <h1 class="text-1xl font-bold bg-clip-text pt-1 text-center">
          Prédit à {{ accessoireprediction }}%
        </h1>
      </div>
    </div>

    <!-- Bloc pour la tenue -->
    <div v-if="tenueprediction !== null" class="flex items-center pt-4">
      <div class="flex flex-col items-center">
        <img
          src="~/../assets/images/Tenue0.svg"
          alt="Logo Tenue"
          class="w-20 h-auto mb-2"
        />
        <h1 class="text-1xl font-bold bg-clip-text pt-1 text-center">
          Prédit à {{ tenautoueprediction }}%
        </h1>
      </div>
    </div>
  </div>
</template>

<script setup>
// Importez les éléments nécessaires et configurez vos propriétés comme vous le faites actuellement.
</script>

<style scoped>
/* Pas besoin de styles spécifiques ici car nous utilisons Tailwind CSS */

/* Vous pouvez également ajouter des classes Tailwind personnalisées si nécessaire */
</style>
