<template>
  <h1 class="text-1xl font-bold text-center">StylAI</h1>
  <div class="flex justify-center">
    <div
      v-if="accessoire !== null"
      class="flex items-center pr-1 pt-4 "
    >
      <div class="flex flex-col items-center ">
        <img
          src="~/../assets/images/Accessoire1.svg"
          alt="Logo Accessoire"
          class="w-20 h-auto mb-2"
        />
      </div>
    </div>
    <div v-if="tenue !== null" class="flex items-center pt-4">
      <div class="flex flex-col items-center">
        <img
          src="~/../assets/images/Tenue0.svg"
          alt="Logo Tenue"
          class="w-20 h-auto mb-2"
        />
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
