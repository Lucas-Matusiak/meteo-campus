<template>
  <div>
    <h1 class="text-3xl font-bold underline">Hello world !</h1>
    <BarreDeRecherche />
  </div>
</template>
<script>
import BarreDeRecherche from '~/components/BarreDeRecherche.vue'

export default {
  components: {
    BarreDeRecherche
  }
  // Autres options du composant parent
}
</script>