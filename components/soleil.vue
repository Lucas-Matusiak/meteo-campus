<template>
  <div
    class="flex flex-col bg-gradient-to-br from-[#469FBB] to-[#8BC5D6]  rounded-lg p-5 m-5"
  >
    <div class="flex items-center pb-5">
      <img
        src="~/../assets/images/lever-soleil.svg"
        alt="Logo Lever du soleil"
        class="w-10"
      />
      <div class=" pl-5">
        <h1 class="text-l">Lever</h1>
        <h1 class="text-2xl font-bold">{{ heureLever }}</h1>
      </div>
    </div>
    <div class="flex items-center">
      <img
        src="~/../assets/images/coucher-soleil.svg"
        alt="Logo Coucher du soleil"
        class="w-10"
      />
      <div class=" pl-5">
        <h1 class="text-l">Coucher</h1>
        <h1 class="text-2xl font-bold">{{ heureCoucher }}</h1>
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
    heureCoucher: { type: String, default: null },
  },
};
</script>
