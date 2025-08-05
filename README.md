
# 🌱 Smart Fertilizer Recommendation System

This project uses Machine Learning to build an intelligent fertilizer recommendation system based on soil conditions, crop type, and weather parameters.

---

## 🚀 Overview

Farmers often lack access to tailored fertilizer recommendations. This system aims to improve agricultural productivity by suggesting the right fertilizer based on:
- Soil nutrients (N, P, K)
- Soil type and moisture
- Temperature and humidity
- Crop type

---

## 📁 Project Structure

```

SmartFertilizerRecommendation/
│
├── data/                   # Dataset files (CSV, JSON, etc.)
├── models/                 # Trained ML models (.pkl)
├── notebooks/              # Jupyter notebooks for EDA and model building
├── app/                    # Streamlit or Flask app files
├── fertilizer\_recommender.py  # Core recommendation logic
├── requirements.txt        # Python dependencies
└── README.md               # Project overview

````

---

## 🧠 ML Models Used

- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors
- (Optional: XGBoost, SVM)

---

## 💾 Dataset

You can start with:
- Kaggle fertilizer prediction datasets
- Synthetic datasets with columns: `N`, `P`, `K`, `temperature`, `humidity`, `moisture`, `soil_type`, `crop_type`, `fertilizer`

---

## 🔧 Installation

```bash
git clone https://github.com/Anand-b-patil/SmartFertilizerRecommendation.git
cd SmartFertilizerRecommendation
pip install -r requirements.txt
````

---

## 💡 How It Works

1. Collect data on soil, weather, and crop
2. Predict suitable fertilizer using trained ML model
3. Show result through a web interface (Streamlit or Flask)

---

## 📈 Future Enhancements

* Real-time weather integration (API)
* GPS-based location-specific recommendations
* Multilingual interface for farmers

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Feel free to fork this repo and submit pull requests. Contributions are welcome!

```




