

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, PositiveInt, computed_field
from loguru import logger
from pathlib import Path
from src.inference import load_model, predict
import pandas as pd


app = FastAPI()
logger.info('Model loading')
project_root = Path.cwd().parent if Path.cwd().stem == 'src' else Path.cwd()
MODEL_PATH = project_root / "models" / "catboost_final"
MODEL = load_model(MODEL_PATH.as_posix())
logger.info('Model loaded')
CITY_MAP = {"Moscow":0, "SPB":1, "Kazan":2}
VEHICLE_MAP = {"scooter":0, "bike":1, "car":2}

class PredictFeatures(BaseModel):
    items_count: PositiveInt
    distance_km: float
    is_express_delivery: bool
    is_fast_food: bool
    prep_time_avg: float
    base_speed_kmh: float
    traffic_level: PositiveInt
    precip_mm: float
    city: str
    vehicle_type: str
    
    @computed_field
    def city_num(self) -> int:
        if self.city in CITY_MAP.keys():
            return CITY_MAP.get(self.city)
        raise ValueError(f'Incorrect city name: {self.city}')
    
    @computed_field
    def vehicle_type_num(self) -> int:
        if self.vehicle_type in VEHICLE_MAP.keys():
            return VEHICLE_MAP.get(self.vehicle_type)
        raise ValueError(f'Incorrect vehicle type: {self.vehicle_type}')
    


class ResponsePrediction(BaseModel):
    delivery_time: float


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/predict", response_model=ResponsePrediction)
def predict_post(features: PredictFeatures):
    """
    Endpoint для получения предсказания ML-модели.

    Parameters
    ----------
    features : PredictFeatures
        Параметры используемые для расчёта времени доставки.

    Returns
    -------
    ResponsePrediction
        Предсказанное время доставки.
    """
    try:
        data = pd.DataFrame([features.model_dump()]).drop(['city', 'vehicle_type'], axis=1)

        # Получаем предсказание модели
        prediction = predict(MODEL, data)[0]

        logger.info(f"Model prediction: {prediction}")

    except Exception as e:
        # Логируем ошибку и возвращаем HTTP 500
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(
            status_code=500,
            detail="Prediction failed"
        )

    # Возвращаем результат в формате Pydantic-модели
    return ResponsePrediction(delivery_time=prediction)


@app.get("/health")
def health():
    return {"status": "ok"}