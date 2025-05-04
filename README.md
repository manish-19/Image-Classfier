# 🖼️ Image Classifier

This is a full-stack image classifier application using:

- **Frontend**: Angular (HTML/CSS)
- **Backend**: FastAPI (Python, REST API)
- **ML**: PyTorch (basic image classification)
- **Database**: CockroachDB
- **Docker**: For containerization

## 🚀 How to Run

### Prerequisites
- Docker and Docker Compose installed

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/your-username/Image-Classfier.git
cd Image-Classfier

# 2. Build and run with Docker
docker-compose up --build
```

### Angular Frontend
- Accessible at `http://localhost:4200`

### FastAPI Backend
- API available at `http://localhost:8000/predict`

### CockroachDB Console
- Visit `http://localhost:8080`

## 📦 Folder Structure

```
Image-Classifier/
├── backend/          # FastAPI + PyTorch + CockroachDB client
├── frontend/         # Angular frontend (HTML/CSS)
├── docker-compose.yml
└── README.md
```

## ✅ Features
- Upload an image through the Angular UI
- Backend predicts the image class using PyTorch ResNet18 model
- Prediction is stored in CockroachDB

---

Made with ❤️ for learning and demo purposes.