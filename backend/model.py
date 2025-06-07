from torchvision import models, transforms
from PIL import Image
import torch
import io

model = models.resnet18(pretrained=True)
model.eval()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
])

def predict_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    tensor = transform(image).unsqueeze(0)
    outputs = model(tensor)
    _, predicted = outputs.max(1)
    return predicted.item()