const backendUrl = "http://127.0.0.1:8000"; // Ajuste para o backend
const express = require('express');
const app = express();

document.getElementById("currentWeatherBtn").addEventListener("click", async () => {
  const city = prompt("Enter a city:");
  if (!city) return alert("City name is required!");
  const resultDiv = document.getElementById("result");
  try {
    const response = await fetch(`${backendUrl}/current-temperature?city=${city}`);
    const data = await response.json();
    resultDiv.innerHTML = `<h2>Current Weather</h2><p>City: ${city}</p><p>Temperature: ${data.temp}°C</p>`;
  } catch (error) {
    resultDiv.innerHTML = `<p>Error fetching current weather: ${error.message}</p>`;
  }
});

document.getElementById("forecastBtn").addEventListener("click", async () => {
  const city = prompt("Enter a city:");
  if (!city) return alert("City name is required!");
  const resultDiv = document.getElementById("result");
  try {
    const response = await fetch(`${backendUrl}/forecast?city=${city}`);
    const data = await response.json();
    let forecastHtml = `<h2>Weather Forecast</h2>`;
    data.forecast.forEach((day) => {
      forecastHtml += `<p>Date: ${day.date} - Temp: ${day.temp}°C</p>`;
    });
    resultDiv.innerHTML = forecastHtml;
  } catch (error) {
    resultDiv.innerHTML = `<p>Error fetching forecast: ${error.message}</p>`;
  }
});

app.use(express.static('public'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

app.listen(3000, () => {
    console.log('Servidor rodando na porta 3000');
});
