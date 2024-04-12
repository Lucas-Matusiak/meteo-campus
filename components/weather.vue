<template>
  <div class="mb-10">
      <div>
        <img 
          src= '../assets/images/ensoleille.png'
          alt="weather"
          class="content-center object-scale-down h-48 w-96"/>
      </div>
      <div >
          <h1 class="text-1xl text-center mb-4"> {{ temps }}</h1>
      </div>
      <div >
          <h1 class="text-2xl  text-center mb-4"> {{ lieu }}</h1>
      </div>
  </div>
</template>

<script>
export default {
  name: 'weather',
   // Renommé pour plus de clarté
  data() {
    return {
      image :2,
      lieu : "Talence Peixotto",
      temps : "Ensoleillé"
  }
}
}
</script>