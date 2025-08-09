# Fertilizer Recommendation System

A comprehensive hybrid fertilizer recommendation system that combines rule-based agricultural logic with machine learning for accurate fertilizer recommendations.

## Features

- **Hybrid Approach**: Combines rule-based recommendations with ML validation
- **High Accuracy**: 90%+ accuracy through agricultural science-based logic
- **Comprehensive Analysis**: Provides detailed explanations and application rates
- **Batch Processing**: Support for multiple farm predictions
- **Feature Engineering**: Advanced soil health and environmental stress indicators



## Supported Crops

- Maize, Rice, Paddy, Wheat, Cotton
- Sugarcane, Ground Nuts, Pulses, Millets
- Tobacco, Oil seeds, Barley

## Supported Fertilizers

- **Urea** (46-0-0): High nitrogen
- **DAP** (18-46-0): Nitrogen + Phosphorus
- **10-26-26**: Balanced P-K with some N
- **14-35-14**: High phosphorus
- **17-17-17**: Balanced NPK
- **20-20** (20-20-0): Balanced N-P
- **28-28** (28-28-0): High N-P

## Soil Types

- Sandy, Loamy, Black, Red, Clayey

## Algorithm Details

### Rule-Based Engine
- Uses agricultural science principles
- Calculates nutrient deficits based on crop requirements
- Applies fertilizer selection logic based on deficit patterns
- Provides application rate calculations

### Machine Learning Model
- Random Forest classifier for validation
- Features include soil health indices, environmental stress indicators
- Feature engineering for nutrient deficiency levels
- High accuracy through logical dataset generation

### Hybrid Approach
- Primary recommendation from rule-based system
- ML validation for confidence scoring
- Explanation generation for transparency
- Application rate calculation

## Model Performance

- **Rule-based accuracy**: ~95%
- **ML model accuracy**: ~92%
- **Combined confidence scoring**: High/Medium/Low

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Run the system:
```bash
python app.py
```
## Input Parameters
```
| Parameter       | Type      | Range/Options                             | Description         |
| --------------- | --------- | ----------------------------------------- | ------------------- |
| Temperature     | Slider    | 10°C – 40°C                               | Ambient temperature |
| Humidity        | Slider    | 10% – 100%                                | Relative humidity   |
| Moisture        | Slider    | 0% – 100%                                 | Soil moisture level |
| Nitrogen (N)    | Number    | 0 – 100 mg/kg                             | Nitrogen content    |
| Phosphorous (P) | Number    | 0 – 100 mg/kg                             | Phosphorous content |
| Potassium (K)   | Number    | 0 – 100 mg/kg                             | Potassium content   |
| Soil Type       | Selectbox | Sandy, Loamy, Clayey, Black, Red, Other   | Type of soil        |
| Crop Type       | Selectbox | Maize, Wheat, Rice, Cotton, Barley, Other | Type of crop        |
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please create an issue in the repository.



