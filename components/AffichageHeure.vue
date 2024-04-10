<template>
  <div>
    <div class="container">
      <div
        :class="{
          'bg-gradient-to-b from-blue-900 to-slate-500': heure >= 0 && heure < 24, // Ensures night class applies for all hours
          'bg-gradient-to-t from-blue-300 to-indigo-500': heure >= 7 && heure < 11,
          'bg-gradient-to-b from-blue-400 to-blue-300': heure >= 11 && heure < 17,
          'bg-gradient-to-b from-blue-300 to-indigo-500': heure >= 17 && heure < 20,
        }"
        class="w-20 h-40 rounded-3xl border flex flex-col items-center justify-center mt-4 mb-4 ml-2 mr-2 "
      >
        <div class="text-black text_xs text-center flex-col">
          <h1 class="text_xs">{{ heure }}:00</h1> 
          <img
              src="~/../assets/images/ensoleille.png"
              alt=""
              class="w-10 h-10 mx-auto"
            />
          <p class="text-xs m-2">{{ temperature }}°</p>
          <div class="flex m-1">
            <img
              src="~/../assets/images/goutteBleue.png"
              alt=""
              class="w-3 h-4 ml-2 mr-1"
            />
            <p class="text-xs mb-1">{{ pourcentagePluie }}%</p>
          </div>
          <div class="flex m-1">
            <img
              src="~/../assets/images/vent.png"
              alt=""
              class="w-4 h-4 ml-1 mr-1"
            />
            <p class="text-xs">{{ vitesseVent }} km/h</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AffichageHeure",
  props: [
    "heure",
    "imgMeteo",
    "temperature",
    "pourcentagePluie",
    "vitesseVent",
  ],
};
</script>
