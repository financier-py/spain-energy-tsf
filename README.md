# Forecasting Spain Power

Тут, полагаю, будет проектик по временным рядам. Планирую провести хороший анализ данных, тесты на стационарность и далее сравнить много разных моделей для данной задачи. Начну с ARIMA и градиентного бустинга, попробую Temporal Fusion Transformer и современные SOTA модельки. 

## Данные 

Kaggle: [`nicholasjhana/energy-consumption-generation-prices-and-weather`](https://www.kaggle.com/datasets/nicholasjhana/energy-consumption-generation-prices-and-weather)

`energy_dataset.csv` - почасовая генерация энергии по разным источникам, их спрос и цены по стране. 

`weather_features.csv` - почасовая погода по городам из Испании.

Данные представлены за 3 года. Они достаточно разнообразные, есть классные фичи, по которым, по ощущениям, можно делать предсказания. Они не самые простые, поэтому я их и взял. 