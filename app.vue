<template>
  <div class="min-h-screen bg-gradient-to-t from-indigo-400 to-sky-50">
    <div class="flex justify-center items-center flex-col p-10">
      <img
        src="~/../assets/images/logo.png"
        alt="Description de l'image"
        class="w-40 sm:w-1/6 lg:w-1/5 m-4"
      />
      <NuxtPage />

      <div class="flex items-center justify-center py-4 mt-10">
        <div class="flex space-x-4">
          <button class="button">Nous contacter</button>
          <button class="button">Mentions légales</button>
          <button class="button">Nos réseaux</button>
        </div>
      </div>
    </div>
  </div>
</template>
