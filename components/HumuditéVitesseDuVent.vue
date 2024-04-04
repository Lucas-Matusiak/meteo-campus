<template>
    <div class="humidity-wind-speed">
      <div class="humidity">
        <img src="~/../assets/images/Humidite.png" alt="Logo Humidité" class="logo" />
        <div>{{ humidite }}%</div>
        <div class="label">Humidité</div>
      </div>
      <div class="wind-speed">
        <img src="~/../assets/images/vent.png" alt="Logo Vitesse du vent" class="logo" />
        <div>{{ vitesseVent }} km/h</div>
        <div class="label">Vitesse du vent</div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HumiditeVitesseDuVent',
    props: {
      humidite: {
        type: Number,
        required: true
      },
      vitesseVent: {
        type: Number,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>
  .humidity-wind-speed {
    display: flex;
    justify-content: space-between; /* Pour aligner les éléments horizontalement */
    align-items: center; /* Pour aligner les éléments verticalement */
  }
  
  .humidity,
  .wind-speed {
    text-align: center;
  }
  
  .logo {
    width: 50px; /* Ajuster la taille des logos selon vos besoins */
  }
  
  .label {
    margin-top: 10px; /* Ajouter un peu plus d'espace entre la valeur et le label */
    margin-left: 5px; /* Ajouter de l'espace entre la valeur et le label */
  }
  
  .humidity {
    margin-right: 1cm; /* Ajouter un espace de 2cm à droite */
  }
  
  .wind-speed {
    margin-left: 1cm; /* Ajouter un espace de 2cm à gauche */
  }
  </style>
  