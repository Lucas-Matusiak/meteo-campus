<template>
  <div class=" items-center justify-center pb-5">
      <div >
          <p class="text-center text-2xl f bg-clip-text text-transparent bg-gradient-to-l from-black to-black "> {{ temperature }}°C </p>     
          <p class="text-center text-1xl  bg-clip-text text-transparent bg-gradient-to-b from-black to-black">Ressenti {{ feelsLike }}°C</p>
      </div>   
  </div>
</template>

  <script>

  export default {
    name: 'Temperature',
    data() {
      return {
        temperature: 19,
        feelsLike: 8,
      }
    }
  }
  </script>