<template>
  <div>
    <img
      src="~/../assets/images/logo.png"
      alt="Description de l'image"
      class="image-top-left"
    />
    <NuxtPage />
  </div> 

  
    <div class="flex items-center justify-center">
      <div class="footer-buttons">
        <button class="button">Nous contacter</button>
        <button class="button">Mentions légales</button>
        <button class="button">Nos réseaux</button>
      </div>
    </div>
  

</template>

<style scoped>
.container {
  position: relative;
  /*display: flex;*/
  display: inline-block;
}
.image-top-left {
  position: relative;
  top: 10px; /* Ajustez selon votre besoin */
  left: 10px; /* Ajustez selon votre besoin */
  width: 100px; /* Ajustez selon la taille de votre image */
  height: auto; /* Ajustez selon la taille de votre image */
}
.footer {
  flex: 1; /* Occupe l'espace restant */
  background-color: #ffffff; /* Couleur du fond */
  padding: 20px 0; /* Espacement intérieur */
  text-align: center;
}

.footer-buttons {
  display: inline-block;
  /*border: 1px solid #000000; /* Bordure du conteneur */
  padding: 10px;
  margin: 0 auto; /* Centre le conteneur horizontalement */
  
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
