from predict import predict_one
from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/predict")
def predict(x: float, y: float, z: float, material: str, complexity: int, process: str):
    time.sleep(5) # Simulate a long computation, we'll motivate this later
    y_pred = predict_one('model.pkl', x, y, z, material, complexity, process)
    return {'time_min': y_pred}

