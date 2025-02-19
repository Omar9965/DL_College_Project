import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

age_model = tf.keras.models.load_model('age_model.h5')
gender_model = tf.keras.models.load_model('gender_model.h5')

def prepare_image(image):
    img = Image.open(image)
    img = img.convert("L")  
    img = img.resize((128, 128))  
    img = np.array(img)
    img = img.reshape((1, 128, 128, 1))  
    img = img / 255.0 
    return img


def prepare_gender_image(image):
    img = Image.open(image)
    img = img.convert('RGB')
    img = img.resize((256, 256))
    img = np.array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

st.title("Age and Gender Prediction from Image")
st.write("Upload an image and the model will predict both age category and gender.")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    resized_display_image = Image.open(uploaded_image).resize((400, 400))
    st.image(resized_display_image, caption="Uploaded Image", width=400)
    
    age_img = prepare_image(uploaded_image)
    age_prediction = age_model.predict(age_img)
    age_category = np.argmax(age_prediction, axis=1)[0] + 1
    age_categories = {1: "Young (0-19)", 2: "Youth (20-40)", 3: "Senior (40-60)", 4: "Old (60+)"}

    gender_img = prepare_gender_image(uploaded_image)
    gender_prediction = gender_model.predict(gender_img)
    gender = "Female" if gender_prediction[0] < 0.5 else "Male"

    st.write(f"Predicted Age Category: {age_categories[age_category]}")
    st.write(f"Predicted Gender: {gender}")
