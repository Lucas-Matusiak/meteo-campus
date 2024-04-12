<template>
  <div class="flex pb-20 ml-5">
    <div class="pr-10 pt-4">
      <img
        src="~/../assets/images/Humidite.png"
        alt="Logo Humidité"
        class="logo"
      />
      <h1 class="text-2xl font-bold bg-clip-text pt-5 text-center">
        {{ humidite }}%
      </h1>
      <h1 class="text-1xl font-bold bg-clip-text text-center">Humidité</h1>
    </div>

    <div class="wind-speed pl-4">
      <img
        src="~/../assets/images/vent.png"
        alt="Logo Vitesse du vent"
        class="logo"
      />
      <h1 class="text-2xl font-bold bg-clip-text pt-5 text-center">
        {{ vitesseVent }} km/h
      </h1>
      <h1 class="text-1xl font-bold bg-clip-text text-center">
        Vitesse du vent
      </h1>
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
