
<template>
  <div class="h-auto flex flex-col justify-center items-center">
    <h1 class="text-4xl font-bold text-center mb-4">Prévisions météo</h1>
    <div class=" "> <!-- Météo  -->
      <div >
        <Temperature/>
      </div>
      <div>
        <HumuditeVitesseDuVent/>
      </div>

    <!-- Bouton pour revenir à l'accueil -->
      <nuxt-link to="/" class=" px-20 py-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out">
        Retour à l'accueil
      </nuxt-link>
    </div>

  </div>
</template>