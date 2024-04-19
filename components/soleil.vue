<template>
    <div class="flex">
      <div class="flex flex-col items-center justify-center bg-gradient-to-b from-[#6FB6D0] to-[#65A0BE] rounded-lg shadow-md w-full max-w-md mx-auto p-4 md:p-6 mr-6 mb-4">
        <img src="~/../assets/images/lever-soleil.svg" alt="Logo Lever du soleil" class=" w-10 " />
        <div class="ml-2">
          <h1 class="text-l font-bold">Lever</h1>
          <h1 class="text-l">{{ heureLever }}</h1>
        </div>

        <img src="~/../assets/images/coucher-soleil.svg" alt="Logo Coucher du soleil" class= "  w-10" />
        <div class="ml-2">
          <h1 class="text-l font-bold">Coucher</h1>
          <h1 class="text-l">{{ heureCoucher }}</h1>
        </div>
      </div>
    </div>
  </template>
  
  <script>
// Définition du composant Vue.js
export default {
  // Déclaration des propriétés du composant
  props: {
    heureLever: { type: String, default: null },
    heureCoucher: { type: String, default: null }
  }
};
</script>
