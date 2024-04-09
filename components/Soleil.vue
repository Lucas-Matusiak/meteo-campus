<template>
    <div class="flex flex-row items-center justify-between pb-20">
      <div class="flex items-center">
        <img src="~/../assets/images/lever-soleil.png" alt="Logo Lever du soleil" class="logo w-10" />
        <div class="ml-2">
          <h1 class="text-lg font-bold">Lever</h1>
          <h1 class="text-lg">{{ heureLever }}</h1>
        </div>
      </div>
      <div class="flex items-center">
        <img src="~/../assets/images/coucher-soleil.png" alt="Logo Coucher du soleil" class="logo w-10" />
        <div class="ml-2">
          <h1 class="text-lg font-bold">Coucher</h1>
          <h1 class="text-lg">{{ heureCoucher }}</h1>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Soleil',
    data() {
      return {
        heureLever: '08:00',
        heureCoucher: '20:00',
      }
    }
  }
  </script>
  