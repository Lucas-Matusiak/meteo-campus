<template>
  <div class="flex pb-20">
    <div class="pr-10 pt-5">
      <div class="flex">
        <div>
          >>>>>>> c7ab811a6f8d840a9cf80abbd7016b38a148556e
          <img
            src="~/../assets/images/Humidite.png"
            alt="Logo Humidité"
            class="logo"
          />
          <h1
            class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-000"
          >
            {{ humidite }}%
          </h1>
          <h1
            class="text-1xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-000"
          >
            Humidité
          </h1>
        </div>
        <div class="wind-speed pl-4">
          <img
            src="~/../assets/images/vent.png"
            alt="Logo Vitesse du vent"
            class="logo"
          />
          <h1
            class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-000"
          >
            {{ vitesseVent }} km/h
          </h1>
          <h1
            class="text-1xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-000"
          >
            Vitesse du vent
          </h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HumiditeVitesseDuVent",
  data() {
    return {
      humidite: 24,
      vitesseVent: 22,
    };
  },
};
</script>
