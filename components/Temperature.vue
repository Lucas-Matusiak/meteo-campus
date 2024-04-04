<template>
    <div>
      <p>{{ temperature }}°C</p>
      <p>Ressenti : {{ feelsLike }}°C</p>
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