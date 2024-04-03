<template>
  <div>
    <img
      src="~/../assets/images/logo.png"
      alt="Description de l'image"
      class="image-top-left"
    />
    <NuxtPage />
  </div>
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
</style>
