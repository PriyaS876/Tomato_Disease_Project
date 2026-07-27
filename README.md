# 🍅 AI-Based Tomato Plant Disease Detection

## 📌 Project Overview

Tomato is one of the most widely cultivated crops in agriculture. However, tomato plants are highly vulnerable to various diseases that can significantly reduce crop yield and quality.

This project presents an **Artificial Intelligence based Tomato Plant Disease Detection System** that automatically identifies diseases from tomato leaf images using **Deep Learning** techniques.

The system uses a **Convolutional Neural Network (CNN)** model trained on tomato leaf images. Users can upload an image of a tomato leaf, and the system will predict the type of disease affecting the plant.

The application is built with **Python, TensorFlow/Keras, and Streamlit** to provide a simple and interactive interface.

---

# 🎯 Objectives

The main objectives of this project are:

* Detect diseases in tomato plant leaves using image classification.
* Assist farmers and researchers in identifying plant diseases quickly.
* Reduce crop loss by enabling early disease detection.
* Build a simple AI-powered application for agricultural use.

---

# 🧠 Technologies Used

| Technology         | Purpose                |
| ------------------ | ---------------------- |
| Python             | Programming Language   |
| TensorFlow / Keras | Deep Learning Model    |
| NumPy              | Numerical computations |
| Matplotlib         | Visualization          |
| Pillow (PIL)       | Image processing       |
| Streamlit          | Web interface          |

---

# 📂 Project Structure

```
Tomato_Disease_Project/
│
├── tomato_disease_model.h5
├── app.py
├── requirements.txt
├── README.md
├── dataset/
│
└── images/
```

### File Description

**app.py**
Main Streamlit application that loads the model and predicts diseases.

**tomato_disease_model.h5**
Trained CNN model used for disease prediction.

**requirements.txt**
Contains all dependencies required to run the project.

**dataset/**
Contains images used for training the model.

---

# 🍃 Diseases Detected

The model can detect the following tomato leaf diseases:

* Tomato Early Blight
* Tomato Late Blight
* Tomato Leaf Mold
* Tomato Septoria Leaf Spot

---

# ⚙️ How the System Works

The system works in the following steps:

### 1️⃣ Image Upload

The user uploads a tomato leaf image through the Streamlit interface.

### 2️⃣ Image Preprocessing

The uploaded image is:

* resized
* converted into an array
* normalized for model input

### 3️⃣ Model Prediction

The trained CNN model analyzes the image and predicts the disease category.

### 4️⃣ Result Display

The predicted disease name is displayed to the user.

---

# 🚀 Installation and Setup

Follow these steps to run the project on your system.

## Step 1: Clone the Repository

```bash
git clone https://github.com/PriyaS876/Tomato_Disease_Project.git
```

## Step 2: Navigate to Project Folder

```bash
cd Tomato_Disease_Project
```

## Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

## Step 4: Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 💻 Running Project Using CMD

If the project is already downloaded on your system, follow these commands:

## Step 1: Open Command Prompt

Go to your project folder location:

```bash
cd "C:\Users\hp\Downloads\AI-Powered-Multi-Crop-Disease-Detection-Smart-Recommendation-System.-main"
```

## Step 2: Check Project Files

```bash
dir
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run Streamlit Application

```bash
streamlit run app.py
```

The application will run on:

```
http://localhost:8501
```

---

# 🖥️ Application Interface

The Streamlit application allows users to:

* Upload tomato leaf images
* View prediction results instantly
* Easily interact with the AI model

---

# 📸 Screenshots

Example:

```
images/app_interface.png
images/prediction_result.png
```

---

# 💡 Key Features

✔ AI-based plant disease detection
✔ User-friendly interface using Streamlit
✔ Fast prediction using CNN model
✔ Image upload functionality
✔ Deep learning based classification

---

# ⚠️ Limitations

- The model works well for tomato leaf disease images, but sometimes it may give wrong predictions for new or different types of leaves.
- Sometimes healthy tomato leaves may be incorrectly classified as diseased leaves due to similarity in leaf patterns.
- The prediction accuracy depends on the quality and variety of images used for training.
- Images with blur, poor lighting, or different backgrounds may affect the prediction results.
- The model may face difficulty with unseen images that are different from the training dataset.
- Adding more diverse images, improving the dataset, and retraining the model can help improve performance.
- Adding more "Other Leaf" images can help the model identify non-tomato leaves better.

---

# 🌱 Future Improvements

This project can be further improved by:

* Adding more plant diseases
* Improving model accuracy with larger datasets
* Deploying the system on cloud platforms
* Creating a mobile application for farmers
* Integrating real-time disease detection

---

# 📊 Real World Applications

* Smart agriculture
* Crop disease monitoring
* Agricultural research
* AI-based farming assistance

---

# 👩‍💻 Author

**Priya Rani**
Computer Science Engineering Student
Lovely Professional University, Punjab

Interested in:

* Data Science
* Artificial Intelligence
* Machine Learning

---

# ⭐ Support

If you like this project, please consider giving it a **⭐ star on GitHub**.

---

# 📜 License

This project is open-source and available under the **MIT License**.
