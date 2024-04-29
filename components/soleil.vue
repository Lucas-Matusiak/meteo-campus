<template>
  <div
    class="bg-opacity-20 bg-indigo-900 backdrop-blur-xl border-opacity-30 rounded-lg shadow-lg text-white rounded-lg p-5 m-5"
  >
    <div class="flex items-center pb-5">
      <img
        src="~/../assets/images/coucher-soleilW.svg"
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
        src="~/../assets/images/lever-soleilW.svg"
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
