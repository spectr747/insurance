# Deployment ML model using Flask and Docker

1. Клонирование репозитория
```
git clone https://github.com/spectr747/insurance.git
```
2. Переход в рабочий каталог
```
cd deploy
```
3. Запуск docker
```
docker build -t insurance:1.0 
docker run -p 5000:3000 insurance:1.0
```
4. Запуск Postman.
```
localhost:5000/predict
```
5. Добавить в Body (raw json):
тестовый набор значений из файла notebook/data/test-data.json
Например:
```
{
  "data": [
    {
      "POLICY_BEGIN_MONTH":2,
      "POLICY_END_MONTH":1,
      "POLICY_SALES_CHANNEL":2,
      "POLICY_SALES_CHANNEL_GROUP":4,
      "POLICY_BRANCH":"Санкт-Петербург",
      "POLICY_MIN_AGE":60,
      "POLICY_MIN_DRIVING_EXPERIENCE":40,
      "VEHICLE_MAKE":"Suzuki",
      "VEHICLE_MODEL":"Grand Vitara",
      "VEHICLE_ENGINE_POWER":140,
      "VEHICLE_IN_CREDIT":0,
      "VEHICLE_SUM_INSURED":535815,
      "POLICY_INTERMEDIARY":"174",
      "INSURER_GENDER":"M",
      "POLICY_CLM_N":"0",
      "POLICY_CLM_GLT_N":"0",
      "POLICY_PRV_CLM_N":"0",
      "POLICY_PRV_CLM_GLT_N":"0",
      "CLIENT_HAS_DAGO":0,
      "CLIENT_HAS_OSAGO":0,
      "POLICY_COURT_SIGN":0,
      "CLAIM_AVG_ACC_ST_PRD":0,
      "POLICY_HAS_COMPLAINTS":0,
      "POLICY_YEARS_RENEWED_N":"3",
      "POLICY_DEDUCT_VALUE":7500,
      "CLIENT_REGISTRATION_REGION":"Санкт-Петербург",
      "POLICY_PRICE_CHANGE":-0.02
    }
  ]
}
```
Нажимаем Send.

В окне Response появится ответ: 
```
{
	'output':{
		'result': 'Принято'
	}
}
```
или
```
{
	'output':{
		'result': 'Отказ'
	}
}
```
