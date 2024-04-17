<template>
    <div class="flex flex-row items-center justify-around">
      <div class="flex items-center justify-center pr-10 pt-4 bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-3xl mb-4 shadow-lg mr-4">
        <img src="~/../assets/images/lever-soleil.png" alt="Logo Lever du soleil" class=" w-10 " />
        <div class="ml-2">
          <h1 class="text-l font-bold">Lever</h1>
          <h1 class="text-l">{{ heureLever }}</h1>
        </div>
      </div>
      <div class="flex items-center justify-center pr-10 pt-4 bg-gradient-to-br from-[#469FBB] to-[#8BC5D6] rounded-3xl mb-4 shadow-lg mr-4">
        <img src="~/../assets/images/coucher-soleil.png" alt="Logo Coucher du soleil" class= "  w-10" />
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
