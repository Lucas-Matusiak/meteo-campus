<template>
  <div
    class="flex justify-center bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-3xl shadow-lg w-[120%]"
  >
    <div class="flex justify-center">
      <!-- Texte Tenue Conseillée au centre -->
      <div class="flex items-center justify-center">
        <h1 class="text-1xl font-bold bg-clip-text text-center">StylAI</h1>
      </div>

      <!-- Bloc pour l'accessoire -->
      <div
        v-if="accessoireprediction !== null"
        class="flex items-center pr-1 pt-4"
      >
        <div class="flex flex-col items-center">
          <img
            src="~/../assets/images/accessoire.png"
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
            src="~/../assets/images/tenue.png"
            alt="Logo Tenue"
            class="w-20 h-auto mb-2"
          />
          <h1 class="text-1xl font-bold bg-clip-text pt-1 text-center">
            Prédit à {{ tenueprediction }}%
          </h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  tenue : String,
  accessoire : String
});
</script>
