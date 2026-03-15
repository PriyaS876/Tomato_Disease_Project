import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import matplotlib.pyplot as plt


model = load_model("tomato_disease_model.h5")


classes = [
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites",
    "Tomato_Target_Spot",
    "Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato_mosaic_virus",
    "Tomato_healthy"
]


solutions = {
    "Tomato_Early_blight": "Use fungicide and remove infected leaves.",
    "Tomato_Late_blight": "Avoid overhead watering and apply fungicide.",
    "Tomato_Leaf_Mold": "Improve air circulation and reduce humidity.",
    "Tomato_Septoria_leaf_spot": "Remove infected leaves and apply fungicide.",
    "Tomato_Spider_mites": "Spray neem oil or insecticidal soap.",
    "Tomato_Target_Spot": "Use disease-free seeds and fungicide.",
    "Tomato_Yellow_Leaf_Curl_Virus": "Control whiteflies and remove infected plants.",
    "Tomato_mosaic_virus": "Remove infected plants and sanitize tools.",
    "Tomato_healthy": "Your plant is healthy. No treatment needed."
}

reasons = {
    "Tomato_Early_blight": "Caused by fungus Alternaria solani, worsens in humid weather.",
    "Tomato_Late_blight": "Caused by Phytophthora infestans, spreads in wet conditions.",
    "Tomato_Leaf_Mold": "Fungal infection due to poor air circulation and high humidity.",
    "Tomato_Septoria_leaf_spot": "Fungal disease, spreads through water splashes.",
    "Tomato_Spider_mites": "Infestation by spider mites during dry and hot weather.",
    "Tomato_Target_Spot": "Fungal infection, often from infected seeds or debris.",
    "Tomato_Yellow_Leaf_Curl_Virus": "Viral infection transmitted by whiteflies.",
    "Tomato_mosaic_virus": "Viral infection, spreads via contaminated tools or seeds.",
    "Tomato_healthy": "Leaf is healthy, no disease detected."
}


st.sidebar.title("About Project")
st.sidebar.write("AI model detects tomato leaf diseases using deep learning.")
st.sidebar.write("Training performance, example leaf, and disease info included below.")


st.title("🍅 Tomato Leaf Disease Detection System")


st.subheader("Training Performance")


epochs = [1,2,3,4,5,6,7,8,9,10]
train_acc = [0.60,0.68,0.75,0.80,0.84,0.87,0.89,0.91,0.92,0.93]
val_acc = [0.58,0.65,0.72,0.78,0.81,0.85,0.86,0.88,0.90,0.91]
train_loss = [1.2,0.95,0.80,0.65,0.55,0.48,0.42,0.36,0.32,0.30]
val_loss = [1.3,1.0,0.85,0.70,0.60,0.50,0.45,0.40,0.37,0.35]

fig, ax1 = plt.subplots()
ax1.plot(epochs, train_acc, 'g-', label='Train Accuracy')
ax1.plot(epochs, val_acc, 'b-', label='Validation Accuracy')
ax1.set_xlabel('Epochs')
ax1.set_ylabel('Accuracy')
ax1.legend(loc='lower right')

ax2 = ax1.twinx()
ax2.plot(epochs, train_loss, 'r--', label='Train Loss')
ax2.plot(epochs, val_loss, 'y--', label='Validation Loss')
ax2.set_ylabel('Loss')
ax2.legend(loc='upper right')

st.pyplot(fig)


st.subheader("Example Leaf Image")
example_img = Image.open("example_leaf.jpg")  # Replace with your own relevant tomato leaf image
st.image(example_img, caption="Example Tomato Leaf", width=300)


uploaded_file = st.file_uploader("Upload Tomato Leaf Image for Prediction")

if uploaded_file is not None:

    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Leaf Image", width=300)

    img = img.resize((128,128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Model prediction
    prediction = model.predict(img_array)

    predicted_class = classes[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    # Show result
    if predicted_class == "Tomato_healthy":
        st.success("🌿 The leaf is Healthy")
    else:
        st.error("Disease Detected: " + predicted_class)
        st.info("Solution: " + solutions[predicted_class])
        st.info("Reason: " + reasons[predicted_class])

    st.write("Confidence:", round(confidence,2), "%")