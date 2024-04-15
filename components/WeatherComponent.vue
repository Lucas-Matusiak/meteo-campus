<template>
  <div>
    <WeatherComponent v-if="weatherData" :data="weatherData" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const lat = ref(48.8566);
const lon = ref(2.3522);
const apiUrlCurrentWeather = 'http://localhost:8080/api/current_weather';
const apiUrlHourlyForecast = 'http://localhost:8080/api/hourly_forecast';
const apiUrlDailyForecast = 'http://localhost:8080/api/daily_forecast';
const apiUrlWeatherDataModel = 'http://localhost:8080/api/weather_data_model';
const weatherData = ref(null);

const getWeatherData = async () => {
  try {
    const responses = await Promise.all([
      axios.get(apiUrlCurrentWeather, { params: { lat: lat.value, lon: lon.value } }),
      axios.get(apiUrlHourlyForecast, { params: { lat: lat.value, lon: lon.value } }),
      axios.get(apiUrlDailyForecast, { params: { lat: lat.value, lon: lon.value } }),
      axios.get(apiUrlWeatherDataModel, { params: { lat: lat.value, lon: lon.value } })
    ]);

    const currentWeatherData = responses[0].data;
    const hourlyForecastData = responses[1].data;
    const dailyForecastData = responses[2].data;
    const weatherDataModelData = responses[3].data;

    weatherData.value = {
      currentWeather: currentWeatherData,
      hourlyForecast: hourlyForecastData,
      dailyForecast: dailyForecastData,
      weatherDataModel: weatherDataModelData
    };
  } catch (error) {
    console.error('Erreur lors de la récupération des données météorologiques :', error);
  }
};

onMounted(() => {
  getWeatherData();
});
</script>
