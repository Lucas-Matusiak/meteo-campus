<template>
<<<<<<< HEAD
  <div class=" items-center justify-center pb-20">
      <div >
          <p class="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-l from-black to-black"> {{ temperature }}°C </p>
           <p class="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-200">Ressenti {{ feelsLike }}°C</p>
=======
  <div class=" items-center justify-center h-screen ">
      <div >
          <p class=" space-x-20 text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-200"> {{ temperature }}°C </p>
           <p class=" space-x-20 text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-200">Ressenti {{ feelsLike }}°C</p>
>>>>>>> c7ab811a6f8d840a9cf80abbd7016b38a148556e
      </div>   
  </div>
</template>

  <script>

  export default {
    name: 'Temperature',
    data() {
      return {
        temperature: 24,
        feelsLike: 22,
      }
    }
  }
  </script>