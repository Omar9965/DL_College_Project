# Gender and Age Classification

This project utilizes deep learning to classify gender and predict age from images. It demonstrates the use of convolutional neural networks (CNNs) for image-based classification tasks and deploys the models via a user-friendly web interface built with Streamlit.

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
  - Young (0-18 years)
  - Youth (18-40 years)
  - Senior (40-60 years)
  - Old (60+ years)

The models are trained using CNNs and deployed using Streamlit for an interactive web interface.

---

## Features
- **Data Processing**: Preprocesses uploaded images for compatibility with the trained models.
- **Gender Classification**: Uses a CNN to predict male or female.
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

To run the application:
1. Start the Streamlit app:
   ```bash
   streamlit run deployment.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```
3. Upload an image, and the application will display the predicted gender and age category.

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
![UI Example](path/to/ui_screenshot.png)

### Predicted Results
- **Input**: Example image of a person.
- **Output**:
  - **Predicted Gender**: Male
  - **Predicted Age Category**: Youth (18-40 years)
