<template>
    <div>
        
      <div class="container mx-auto">
        <div
        :class="{
          'bg-blue-900':heure < 8,
          'bg-gradient-to-tr from-blue-500 via-sky-700 to-blue-900': heure >= 8 && heure < 12,
          'bg-gradient-to-br from-blue-500 via-sky-700 to-blue-900': heure >= 12 && heure < 17,
          'bg-gradient-to-t from-blue-900 via-sky-700 to-blue-500': heure >= 17 && heure < 20,
          'bg-blue-900': heure >= 20,
        }"
          class="w-20 h-40 rounded-lg border flex flex-col items-center justify-center m-1"
        >
          <div class="text-black text-center">
            <p class="text_base">{{heure}} h</p>
            <p class="text-base">{{temperature}}°</p>
            <p class="text-base">{{ pourcentagePluie }}%</p>
            <p class="text-base">{{vitesseVent}} km/h</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  <script>
  export default {
    name: "AffichageHeure",
    props: ["heure","temperature","pourcentagePluie","vitesseVent"],
  };
  </script>
  