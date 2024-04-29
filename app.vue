<template>
  <div class="min-h-screen bg-gradient-to-r from-sky-500 to-indigo-500 text-white">
    <div class="flex justify-center items-center flex-col p-10 ">
      <img
        src="~/../assets/images/MeteoCampus_White.svg"
        alt="Description de l'image"
        class="w-20 h-auto m-4"
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
