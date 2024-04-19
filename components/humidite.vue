<template>
  <div class="flex justify-center">
    <div class="pt-4">
      <div v-if="humidite !== null">
        <img
          src="~/../assets/images/Humidite.png"
          alt="Logo Humidité"
          class="logo"
        />
        <h1 class="text-2xl font-bold bg-clip-text pt-5 text-center">{{ humidite }}%</h1>
        <h1 class="text-1xl font-bold bg-clip-text text-center">Humidité</h1>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    humidite: { type: String, default: null },
  },
};
</script>
