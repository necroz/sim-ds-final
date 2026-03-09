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
git clone https://github.com/totiela/sim-ds-model-as-a-service
```

---

### 2️⃣ Создание виртуального окружения

#### 🪟 Windows (PowerShell)

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> ⚠️ Если PowerShell ругается на политику выполнения:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

#### 🍎 macOS / 🐧 Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3️⃣ Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## 🚀 Запуск FastAPI

```bash
uvicorn src.main:app --reload --port 8000
```

API будет доступно по адресу:

👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📚 Swagger / OpenAPI

FastAPI автоматически генерирует документацию:

- Swagger UI:
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

- OpenAPI schema:
  👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

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
