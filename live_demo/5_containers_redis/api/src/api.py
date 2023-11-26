from predict import predict_one
from fastapi import FastAPI
import redis
import time

# Host is the container name - docker compose automatically takes care of networking containers from the same docker-compose.yml file
r = redis.Redis(host='shiny-redis-cache', port=6379, decode_responses=True)
app = FastAPI()

@app.get("/predict")
def predict(x: float, y: float, z: float, material: str, complexity: int, process: str):
    key = f'{x}-{y}-{z}-{material}-{complexity}-{process}'
    if r.exists(key):
        return {'time_min': float(r.get(key))}
    time.sleep(5) # Simulate a long computation, we'll motivate this later
    y_pred = predict_one('model.pkl', x, y, z, material, complexity, process)
    r.set(key, y_pred)
    return {'time_min': y_pred}

