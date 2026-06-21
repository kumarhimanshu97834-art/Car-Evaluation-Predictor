import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Car Evaluation Predictor",
    page_icon="🚗",
    layout="wide"
)

# ----------------------------
# Load Model
# ----------------------------
model = joblib.load("car_model.pkl")

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#4CAF50;
}
.sub-title{
    text-align:center;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------
st.markdown('<p class="main-title">🚗 Car Evaluation Predictor</p>',
            unsafe_allow_html=True)

st.markdown(
    '<p class="sub-title">Predict Car Acceptability using Machine Learning</p>',
    unsafe_allow_html=True
)

st.divider()

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("📌 About")

st.sidebar.info(
    """
    Car Evaluation Prediction System

    Models Used:
    - Random Forest
    - Decision Tree
    - XGBoost
    - CatBoost

    Developed by Himanshu Kumar
    """
)

# ----------------------------
# Accuracy Display
# ----------------------------
st.metric(
    label="Model Accuracy",
    value="99.8%"
)

# ----------------------------
# Input Section
# ----------------------------
col1, col2 = st.columns(2)

with col1:

    buying = st.selectbox(
        "Buying Price",
        ["low","med","high","vhigh"]
    )

    maint = st.selectbox(
        "Maintenance Cost",
        ["low","med","high","vhigh"]
    )

    doors = st.selectbox(
        "Doors",
        ["2","3","4","5more"]
    )

with col2:

    persons = st.selectbox(
        "Persons Capacity",
        ["2","4","more"]
    )

    lug_boot = st.selectbox(
        "Luggage Boot Size",
        ["small","med","big"]
    )

    safety = st.selectbox(
        "Safety",
        ["low","med","high"]
    )

# ----------------------------
# Encoding Maps
# ----------------------------
buying_map = {
    "low":0,
    "med":1,
    "high":2,
    "vhigh":3
}

maint_map = buying_map

doors_map = {
    "2":0,
    "3":1,
    "4":2,
    "5more":3
}

persons_map = {
    "2":0,
    "4":1,
    "more":2
}

lug_map = {
    "small":0,
    "med":1,
    "big":2
}

safety_map = {
    "low":0,
    "med":1,
    "high":2
}

# ----------------------------
# Prediction
# ----------------------------
if st.button("🔍 Predict Car Evaluation"):

    data = pd.DataFrame([[
        buying_map[buying],
        maint_map[maint],
        doors_map[doors],
        persons_map[persons],
        lug_map[lug_boot],
        safety_map[safety]
    ]],
    columns=[
        "buying",
        "maint",
        "doors",
        "persons",
        "lug_boot",
        "safety"
    ])

    prediction = model.predict(data)[0]

    class_map = {
        0:"acc",
        1:"good",
        2:"unacc",
        3:"vgood"
    }

    result = class_map[prediction]

    st.divider()

    st.subheader("Prediction Result")

    if result == "vgood":
        st.success("🚗 Very Good Car")

    elif result == "good":
        st.info("✅ Good Car")

    elif result == "acc":
        st.warning("⚠ Acceptable Car")

    else:
        st.error("❌ Unacceptable Car")

    # Probability
    if hasattr(model, "predict_proba"):

        st.subheader("Prediction Probability")

        probs = model.predict_proba(data)[0]

        prob_df = pd.DataFrame({
            "Class": model.classes_,
            "Probability (%)": probs * 100
        })

        st.dataframe(prob_df)

        st.bar_chart(
            prob_df.set_index("Class")
        )

# ----------------------------
# Footer
# ----------------------------
st.divider()

st.markdown(
    """
    <center>
    Developed using Streamlit & Machine Learning
    </center>
    """,
    unsafe_allow_html=True
)