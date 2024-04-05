<template>
  <div class="m-8 flex justify-center items-center flex-col">
    <RechercheCampus @university-selected="updateUniversity" />
    <button @click="allerVersProchainePage" class="px-6 py-3 bg-blue-500 text-white font-bold rounded-full hover:bg-blue-700 transition duration-300 ease-in-out">
      Voir les infos météo
    </button>
  </div>
</template>

<script>
import RechercheCampus from "~/components/RechercheCampus.vue";
import { useRouter } from 'vue-router';
import { ref } from 'vue';

export default {
  components: {
    RechercheCampus
  },
  setup() {
    const router = useRouter();
    const selectedUniversity = ref('');

    const updateUniversity = (value) => {
      selectedUniversity.value = value;
    };

    const allerVersProchainePage = () => {
      router.push({ name: 'meteo', query: { selectedUniversity: selectedUniversity.value } });
    };

    return {
      updateUniversity,
      allerVersProchainePage
    };
  }
};
</script>
