from fastapi import FastAPI, UploadFile, File
from model import predict_image
from database import save_prediction

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    label = predict_image(image_bytes)
    save_prediction(label)
    return {"label": str(label)}