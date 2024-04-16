<template>
    <div class="flex flex-row items-center justify-around">
      <div class="flex items-center">
        <img src="~/../assets/images/lever-soleil.png" alt="Logo Lever du soleil" class="logo w-10" />
        <div class="ml-2">
          <h1 class="text-lg font-bold">Lever</h1>
          <h1 class="text-lg">{{ heureLever }}</h1>
        </div>
      </div>
      <div class="flex items-center">
        <img src="~/../assets/images/coucher-soleil.png" alt="Logo Coucher du soleil" class="logo w-10" />
        <div class="ml-2">
          <h1 class="text-lg font-bold">Coucher</h1>
          <h1 class="text-lg">{{ heureCoucher }}</h1>
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
