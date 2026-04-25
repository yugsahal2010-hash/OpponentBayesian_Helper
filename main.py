from fastapi import FastAPI
import math

app = FastAPI()

@app.post("/credibility")
def credibility(payload: dict):
    overall_std = payload["overall_std"]
    opponent_std = payload["opponent_std"]
    result = (overall_std / opponent_std) ** 2
    return {"result": result}
