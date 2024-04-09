<template>
  <div class=" items-center justify-center pb-20">
      <div >
          <p class="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-l from-black to-black"> {{ temperature }}°C </p>           <p class="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-b from-black to-black">Ressenti {{ feelsLike }}°C</p>
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