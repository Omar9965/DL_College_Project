# Gender and Age Classification


This project leverages deep learning to classify gender and predict age from images. It utilizes a custom CNN for age prediction and a pre-trained VGG16 model for gender classification. The models are deployed through a user-friendly web interface built using Streamlit

---

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Example Output](#example-output)

---

## About the Project
The **Gender and Age Classification** project is a tool that predicts:
- **Gender**: Identifies if the person in the image is male or female.
- **Age Category**: Classifies the age into one of the following categories:
  - Young (0-19 years)
  - Youth (20-40 years)
  - Senior (40-60 years)
  - Old (60+ years)

The age prediction model is built using a custom CNN architecture, while the gender classification model leverages the pre-trained VGG16 . Both models are deployed using Streamlit to provide an interactive web interface.

---

## Features
- **Data Processing**: Preprocesses uploaded images for compatibility with the trained models.
- **Gender Classification**: Uses the pre-trained VGG16 model to predict male or female.
- **Age Categorization**: Uses another CNN to classify age into predefined categories.
- **Web Application**: Provides an intuitive interface for uploading images and viewing results.

---

## Getting Started

Follow these steps to set up and run the project locally:

### Prerequisites
- Python 3.7+
- Streamlit library
- Pre-trained models (`age_model.h5` and `gender_classification_cnn_model.h5`)

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd Gender_and_Age_Classification
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the pre-trained models are in the project directory:
   - `age_model.h5`: For age prediction.
   - `gender_classification_cnn_model.h5`: For gender classification.

---

## Usage

To use the application, follow these steps:

1. Open the web application directly by clicking [here](https://dlcollegeproject-rnd5mrgjsndejpbhpatljp.streamlit.app/).
2. Upload an image using the provided interface.
3. The application will process the image and display the predicted gender and age category.
 ![Project Demo](https://raw.githubusercontent.com/m7md158/DL_Colloge_Project/main/Recording2024-12-27122259-ezgif.com-video-to-gif-converter.gif)


---

## Project Structure
The project files are organized as follows:
```
Gender_and_Age_Classification/
├── Age_model.ipynb               # Notebook for training the age prediction model
├── Gender_model_vgg16-cnn.ipynb  # Notebook for training the gender classification model
├── deployment.py                 # Streamlit application script
├── requirements.txt              # Python dependencies file
├── age_model.h5                  # Pre-trained age prediction model
├── gender_classification_cnn_model.h5  # Pre-trained gender classification model
└── README.md                     # Project documentation
```

---

## Example Output

### User Interface
(Placeholder for UI screenshot)
![Screenshot](https://raw.githubusercontent.com/m7md158/DL_Colloge_Project/main/Screenshot%202024-12-27%20130946.png)


### Predicted Results

