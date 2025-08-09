import streamlit as st

from fertilizer_recommender import ImprovedFertilizerRecommender

recommender = ImprovedFertilizerRecommender()

st.set_page_config(
    page_title="🍃 Smart Fertilizer Recommender",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 18px;
        color: #555555;
        text-align: center;
        margin-bottom: 40px;
    }
    .result-box {
        background-color: #f0f8ff;
        border-radius: 8px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 8px rgba(46,139,87,0.2);
    }
    .footer {
        font-size: 14px;
        color: #777777;
        text-align: center;
        margin-top: 40px;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌿 Fertilizer Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter soil and crop parameters to get smart fertilizer advice.</div>', unsafe_allow_html=True)

st.sidebar.header("Input Parameters")

temperature = st.sidebar.slider('Temperature (°C)', 10, 40, 25, help="Ambient temperature of the location")
humidity = st.sidebar.slider('Humidity (%)', 10, 100, 50, help="Relative humidity percentage")
moisture = st.sidebar.slider('Soil Moisture (%)', 0, 100, 40, help="Current soil moisture level")
nitrogen = st.sidebar.number_input('Nitrogen (N, mg/kg)', 0, 100, 15)
phosphorous = st.sidebar.number_input('Phosphorous (P, mg/kg)', 0, 100, 20)
potassium = st.sidebar.number_input('Potassium (K, mg/kg)', 0, 100, 25)

soil_type = st.sidebar.selectbox('Soil Type', ['Sandy', 'Loamy', 'Clayey', 'Black', 'Red', 'Other'])
crop_type = st.sidebar.selectbox('Crop Type', ['Maize', 'Wheat', 'Rice', 'Cotton', 'Barley', 'Other'])

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    recommend_btn = st.button('Get Fertilizer Recommendation')

if recommend_btn:
    result = recommender.predict(
        temperature=temperature,
        humidity=humidity,
        moisture=moisture,
        nitrogen=nitrogen,
        phosphorous=phosphorous,
        potassium=potassium,
        soil_type=soil_type,
        crop_type=crop_type
    )

    st.subheader("✅ Recommendation Result")
    st.markdown(f"### 🌱 Fertilizer Recommendation: **{result['primary_recommendation']}**")
    

    st.markdown(f"**Confidence Level:**  {result['confidence']}")
    
    st.markdown(f"**Explanation:** {result['explanation']}")

st.markdown("""
---
<div class="footer">
If the recommendation seems off, double-check soil test values and crop type.<br>
For critical decisions, always consult an agriculture expert.
</div>
""", unsafe_allow_html=True)
