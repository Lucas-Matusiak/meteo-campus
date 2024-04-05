<template>
  <div class=" items-center justify-center pb-20">
      <div >
          <p class="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-200"> {{ temperature }}°C </p>
           <p class="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-white-200">Ressenti {{ feelsLike }}°C</p>
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