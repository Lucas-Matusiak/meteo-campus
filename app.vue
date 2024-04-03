<template>
  <div>
    <img
      src="~/../assets/images/logo.png"
      alt="Description de l'image"
      class="image-top-left"
    />
    <NuxtPage />
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

<style scoped>
.container {
  position: relative;
}

.image-top-left {
  position: relative;
  top: 10px; /* Ajustez selon votre besoin */
  left: 10px; /* Ajustez selon votre besoin */
  width: 100px; /* Ajustez selon la taille de votre image */
  height: auto; /* Ajustez selon la taille de votre image */
}
.footer {
  background-color: #ffffff; /* Couleur blanche */
  padding: 20px 0; /* Espacement intérieur */
  text-align: center;
}

.footer-buttons {
  display: flex;
  justify-content: center;
  margin: 0 auto; /* Alignement horizontal au centre */
  
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
