# 🚀 Model as a Service (FastAPI)

Пример реализации подхода **Model as a Service (MaaS)** для задач машинного обучения.
Проект демонстрирует, как обученную ML-модель обернуть в REST API с использованием **FastAPI**.

Модель принимает признаки доставки и возвращает предсказанное время.

---

## 📁 Структура проекта

```text
sim-ds-final/
├── models/
│   └── catboost_final          # Сохранённая ML-модель
│
├── src/
│   ├── __init__.py
│   ├── main.py                # FastAPI-приложение (entrypoint)
│   ├── inference.py          # Загрузка модели
│
├── tests/                    # (опционально) тесты
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 Архитектура

**Pipeline:**

1. `catboost_final` — сохранённая модель

**Inference / API:**

- `inference.py` — загрузка модели и предсказание
- `app.py` — REST API (FastAPI)

---

## 🛠️ Установка и запуск

### 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/necroz/sim-ds-final
```

---

## 🚀 Запуск FastAPI в Docker контейнере

```bash
docker build -t fastapi-predictor .
```

```bash
docker run --name my_fastapi_predictor -p 8000:8000 fastapi-predictor
```

API будет доступно по адресу:

👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔮 Пример запроса

### POST `/predict`

**Request body:**

```json
{
  "items_count": 4,
  "distance_km": 5.29,
  "is_express_delivery": true,
  "is_fast_food": false,
  "prep_time_avg": 16,
  "base_speed_kmh": 40.610124,
  "traffic_level": 3,
  "precip_mm": 4.66,
  "city": "Moscow",
  "vehicle_type": "car"
}
```

**Response:**

```json
{
  "delivery_time": 75.95944098946629
}
```

---

## 🧩 Используемые технологии

- Python 3.10+
- FastAPI
- Pydantic
- Mlflow
- Pandas
- Catboost
- Uvicorn
- Loguru
