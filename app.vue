<template>
  <div>
    <h1 class="text-3xl font-bold underline">Hello world !</h1>
    <BarreDeRecherche />
  </div>

  <footer class="footer">
    <div class="container">
      <div class="footer-buttons">
        <button class="button">Nous contacter</button>
        <button class="button">Mentions légales</button>
        <button class="button">Nos réseaux</button>
      </div>
    </div>
  </footer>

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

<style>
.footer {
  background-color: #ffffff; /* Couleur blanche */
  padding: 20px 0; /* Espacement intérieur */
  text-align: center;
}

.footer-buttons {
  display: flex;
  justify-content: center;
}

.button {
  background-color: #ffffff; /* Couleur blanche */
  color: #000000; /* Couleur noire */
  border: none;
  padding: 10px 20px;
  margin: 0 10px;
  cursor: pointer;
  border-radius: 5px;
  outline: none;
}
</style>
