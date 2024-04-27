<template>
  <img :src="getIconPath()" alt="Weather Icon"
    :class="{ 'w-12 h-12': size === 'small', 'w-15 h-15': !size || size === 'default', 'w-100 h-100' : size === 'large' }" />
</template>

<script setup>
import { ref, computed } from "vue";

const props = defineProps({
  code: String,
  size: {
    type: String,
    default: 'default',
    validator(value) {
      return ['small', 'default', 'large'].includes(value);
    },
  },
});

const svgMap = {
  '01d': '/images/01d.svg',
  '01n': '/images/01n.svg',
  '02d': '/images/02d.svg',
  '02n': '/images/02n.svg',
  '03d': '/images/03d.svg',
  '03n': '/images/03n.svg',
  '04d': '/images/04d.svg',
  '04n': '/images/04n.svg',
  '09d': '/images/09d.svg',
  '09n': '/images/09n.svg',
  '10d': '/images/10d.svg',
  '10n': '/images/10n.svg',
  '11d': '/images/11d.svg',
  '13d': '/images/13d.svg',
  '13n': '/images/13n.svg',
  '50d': '/images/50d.svg',
  '50n': '/images/50n.svg',
  'default': 'images/01d.svg',
};

const getIconPath = () => {
  return svgMap[props.code] || svgMap['default'];
};
</script>