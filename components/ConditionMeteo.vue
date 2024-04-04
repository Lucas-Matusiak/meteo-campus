<template>
  <div id="weather">
    <img
      :src="weatherImage"
      alt="weather"
      class="w-20 h-auto m-4"
    />
  </div>
</template>
<script>
// Importation des images en haut du fichier
import ensoleilleImg from '~/../assets/images/logo.png';
import nuageuxImg from '~/../assets/images/logo.png';
import pluvieuxImg from '~/../assets/images/logo.png';
import defaultImg from '~/../assets/images/logo.png';

export default {
  name: 'ConditionMeteo',
  props: {
    condition: String
  },
  computed: {
    weatherImage() {
      switch (this.condition.toLowerCase()) {
        case 'ensoleille':
          return ensoleilleImg;
        case 'nuageux':
          return nuageuxImg;
        case 'pluvieux':
          return pluvieuxImg;
        default:
          return defaultImg;
      }
    }
  }
}

<style>
#weather {
  display: flex;
  justify-content: center;
}
</style>
