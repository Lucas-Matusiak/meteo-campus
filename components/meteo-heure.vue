<template>
  <div>
    <div class="container mx-auto">
      <div
        class="w-20 h-40 bg-gradient-to-b from-orange-400 via-orange-200 to-orange-50 rounded-lg border flex flex-col items-center justify-center m-10"
      >
        <div class="text-black text-center">
          <p class="text_base">{{heure}} h</p>
          <p class="text-base">{{temperature}}°</p>
          <p class="text-base">{{ pourcentagePluie }}%</p>
          <p class="text-base">{{vitesseVent}}km/h</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "MeteoHpH",
  data() {
    return {
      heure: 12,
      temperature:20,
      pourcentagePluie : 0.1*100,
      vitesseVent: 5.6*3.6,
    };
  },
};
</script>
