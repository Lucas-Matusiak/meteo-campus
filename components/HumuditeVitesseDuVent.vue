<template>
    <div class= "flex">
      <div >
        <img src="~/../assets/images/Humidite.png" alt="Logo Humidité" class="logo" />
        <h1 class ="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-000">{{ humidite }}%</h1>
        <h1 class="text-1xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-000">Humidité</h1>
      </div>
      <div class="wind-speed">
        <img src="~/../assets/images/vent.png" alt="Logo Vitesse du vent" class="logo" />
        <h1 class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-000">{{ vitesseVent }} km/h</h1>
        <h1 class="text-1xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-000">Vitesse du vent</h1>
      </div>
    </div>
  </template>
  
  <script>

export default {
    name: 'HumiditeVitesseDuVent',
    data() {
      return {
        humidite: 24,
        vitesseVent: 22,
      }
    }
  }
  </script>
  
 