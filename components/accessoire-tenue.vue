<template>
  <h1 class="text-1xl font-bold text-center">StylAI</h1>
  <div class="flex justify-center">
    <div v-if="accessoire" class="flex items-center pr-1 pt-4">
      <div class="flex flex-col items-center">
        <img
          src="~/../assets/images/Accessoire1W.svg"
          alt="Logo Accessoire"
          :class="{
            'w-12 h-auto mb-2': size === 'small',
            'w-20 h-auto mb-2': !size || size === 'default',
            'w-100 h-auto mb-2': size === 'large',
          }"
        />
        <h1>Accessoire</h1>
      </div>
    </div>
    <div v-if="tenue" class="flex items-center pt-4">
      <div class="flex flex-col items-center">
        <img
          src="~/../assets/images/Tenue0W.svg"
          alt="Logo Tenue"
          class="w-20 h-auto mb-2"
        />
        <h1>Tenue</h1>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  tenue: String,
  accessoire: String,
  size: {
    type: String,
    default: "default",
    validator(value) {
      return ["small", "default", "large"].includes(value);
    },
  },
});
const svgMap = {
  "0t": "/images/Tenue0W.svg",
  "1t": "/images/Tenue1W.svg",
  "2t": "/images/Tenue2W.svg",
  "3t": "/images/Tenue3W.svg",
  "1a": "/images/Accessoire1W.svg",
  "2a": "/images/Accessoire2W.svg",
  "3a": "/images/Accessoire3W.svg",
  default: "/images/unknow.svg",
};
const getIconPath = () => {
  return svgMap[props.code] || svgMap["default"];
};
</script>
