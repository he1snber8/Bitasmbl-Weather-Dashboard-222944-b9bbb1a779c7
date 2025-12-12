# Bitasmbl-Weather-Dashboard-222944-b9bbb1a779c7

## Description
Build a web application that displays current weather, multi-day forecasts, and visualizes trends with charts. The project focuses on integrating APIs, dynamic front-end updates, and data visualization for an interactive user experience.

## Tech Stack
- ASP.NET Core
- Vue.js
- Flask

## Requirements
- Fetch real-time weather data from a public API
- Display multi-day weather forecasts with clear UI elements
- Visualize temperature, humidity, or other metrics with charts
- Support user interactions, such as searching by city
- Optionally cache API responses to improve performance

## Installation
bash
git clone https://github.com/he1snber8/Bitasmbl-Weather-Dashboard-222944-b9bbb1a779c7.git
cd Bitasmbl-Weather-Dashboard-222944-b9bbb1a779c7

ASP.NET Core:
bash
dotnet restore

Vue.js:
bash
npm install

Flask:
bash
pip install -r requirements.txt


## Usage
ASP.NET Core:
bash
dotnet run

Vue.js:
bash
npm run dev

Flask:
bash
flask run


## Implementation Steps
1. Configure ASP.NET Core, Vue.js, and Flask project structures.
2. Integrate a public weather API for real-time data.
3. Implement city search and request handling.
4. Build UI components for current and multi-day forecasts in Vue.js.
5. Implement chart-based visualization of weather metrics.
6. Add optional caching of API responses.
7. Connect front-end components to back-end endpoints.

## API Endpoints
- GET /weather/current
- GET /weather/forecast