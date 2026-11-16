import requests

WEATHER_CODES = {
    0: "☀️ Ясно",
    1: "🌤️ Преимущественно ясно",
    2: "⛅ Переменная облачность",
    3: "☁️ Пасмурно",
    45: "🌫️ Туман",
    48: "🌫️ Иней",
    51: "🌦️ Легкая морось",
    53: "🌦️ Морось",
    55: "🌧️ Сильная морось",
    61: "🌧️ Небольшой дождь",
    63: "🌧️ Дождь",
    65: "🌧️ Сильный дождь",
    71: "🌨️ Небольшой снег",
    73: "🌨️ Снег",
    75: "🌨️ Сильный снег",
    80: "🌦️ Ливень",
    95: "⛈️ Гроза",
    96: "⛈️ Гроза с градом"
}

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT = 10


def get_city_coordinates(city_name):
    params = {
        "name": city_name,
        "count": 1,
    }
    try:
        response = requests.get(GEOCODING_URL, params=params, timeout=TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Ошибка: превышено время ожидания запроса упс.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Ошибка HTTP при запросе координат: {e}")
        return None
    except requests.exceptions.ConnectionError:
        print("Ошибка сети: не получилось подключиться к серверу :(((( .")
        return None

    try:
        data = response.json()
    except ValueError:
        print("Ошибка: сервер вернул какой-то сломанный JSON.")
        return None

    results = data.get("results")
    if not results:
        print(f"Город '{city_name}' не найден. Будьте добры проверить правильность написания.")
        return None

    first = results[0]
    try:
        lat = first["latitude"]
        lon = first["longitude"]
    except KeyError:
        print("Ошибка: в ответе отсутствуют координаты города.")
        return None

    return lat, lon

def get_weather(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
    }
    try:
        response = requests.get(FORECAST_URL, params=params, timeout=TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Ошибка: слишком долго ожидаем....")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Ошибка HTTP при запросе погоды: {e}")
        return None
    except requests.exceptions.ConnectionError:
        print("Ошибка сети: не удалось подключиться к серверу блин.")
        return None

    try:
        data = response.json()
    except ValueError:
        print("Ошибка: сервер вернул не очень классный JSON.")
        return None

    current = data.get("current")
    if not current:
        print("Ошибка: в ответе инфы о текущей погоде.")
        return None
    return current


def decode_weather_code(code):
    if code in WEATHER_CODES:
        return WEATHER_CODES[code]
    return f"Неизвестные условия (код: {code})"


def format_weather_output(city, weather_data):
    temperature = weather_data.get("temperature_2m")
    humidity = weather_data.get("relative_humidity_2m")
    wind_speed = weather_data.get("wind_speed_10m")
    weather_code = weather_data.get("weather_code")

    condition = decode_weather_code(weather_code)


    if temperature is not None:
        sign = "+" if temperature >= 0 else ""
        temp_str = f"{sign}{temperature}°C"
    else:
        temp_str = "н/д"

    lines = [
        f"Погода в городе: {city}",
        f"Температура:  {temp_str}",
        f"Влажность:     {humidity}%",
        f"Ветер:         {wind_speed} км/ч",
        f"Состояние:    {condition}",
    ]
    return "\n".join(lines)

city_name = input("Введите название города на английском (например, Moscow, London, Tokyo): ").strip()
if not city_name:
    print("Ошибка: название города не может быть пустым.")
coords = get_city_coordinates(city_name)
lat, lon = coords
weather_data = get_weather(lat, lon)
print()
print(format_weather_output(city_name, weather_data))
