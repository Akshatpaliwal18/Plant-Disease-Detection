import os
import json
from PIL import Image
import numpy as np
import tensorflow as tf
import streamlit as st


#MY INFO
st.sidebar.title("About the Developer")
st.sidebar.write("Akshat Paliwal")
st.sidebar.write("A010145023183")
st.sidebar.write("Amity University Noida, AIIT")
st.sidebar.write("Contact +91 98685 66339")
st.sidebar.title("About Project")
st.sidebar.write("This project utilizes a deep learning model to classify plant diseases by analyzing leaf images. By leveraging image processing and neural networks, it provides accurate disease predictions, aiding farmers and researchers in early detection and treatment. The system enhances agricultural productivity by offering an efficient, AI-driven plant health assessment tool..")


working_dir = os.path.dirname(os.path.abspath(__file__))

#  file paths
model_path = os.path.join(working_dir, "plant_disease_prediction_model.h5")
class_indices_path = os.path.join(working_dir, "class_indices.json")

# Loading trained model
model = tf.keras.models.load_model(model_path)


with open(class_indices_path, "r") as f:
    class_indices = json.load(f)


def load_and_preprocess_image(image, target_size=(224, 224)):
    img = Image.open(image)  
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.
    return img_array

def predict_image_class(model, image, class_indices):
    preprocessed_img = load_and_preprocess_image(image)
    predictions = model.predict(preprocessed_img)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)]
    return predicted_class_name


st.title("Identification Of Plants And Fruit Diseases Using ML.")
st.write("Upload an image of a plant leaf, and the model will classify the disease.")

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)

    with col1:
        resized_img = image.resize((150, 150))
        st.image(resized_img)

    with col2:
        try:

            if st.button('Classify'):
                prediction = predict_image_class(model, uploaded_image, class_indices)
                st.success(f'Prediction: {str(prediction)}')
        except Exception as e:
            st.error(f"Model Not Found Something Wrong in Image")
