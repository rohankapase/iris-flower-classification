# 🌸 Iris Flower Classification Using KNN

## Project Overview

This project focuses on **classifying Iris flowers** into three species (*Setosa*, *Versicolor*, and *Virginica*) using **machine learning (K-Nearest Neighbors)**.
The goal is to predict the species based on the flower's **sepal and petal measurements**, demonstrating a complete workflow of a supervised learning problem.

---

## Objectives

* Train a KNN model to classify Iris flowers
* Evaluate model performance using accuracy
* Allow interactive predictions based on user input
* Demonstrate supervised learning and data preprocessing concepts

---

## Dataset

The dataset contains **150 samples** with the following features:

| Feature           | Description                                        |
| ----------------- | -------------------------------------------------- |
| Sepal Length (cm) | Length of the sepal                                |
| Sepal Width (cm)  | Width of the sepal                                 |
| Petal Length (cm) | Length of the petal                                |
| Petal Width (cm)  | Width of the petal                                 |
| Species           | Target label (*Setosa*, *Versicolor*, *Virginica*) |

> Make sure `Iris.csv` is in the project folder before running the script.

---

## Technologies Used

* Python 🐍
* Pandas
* NumPy
* Scikit-learn

---

## Key Concepts

* Data Cleaning & Preprocessing
* Train-Test Split
* K-Nearest Neighbors (KNN)
* Model Evaluation (Accuracy)
* Interactive Prediction

---

## Project Workflow

1. Load and preprocess the dataset
2. Split data into training and testing sets
3. Train KNN classifier on training data
4. Evaluate the model on test data
5. Allow users to input custom measurements for prediction

---

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/rohankapase/Iris-Flower-Classification.git
```

2. Navigate to the project folder:

```bash
cd Iris-Flower-Classification
```

3. Install required packages:

```bash
pip install pandas scikit-learn
```

4. Run the Python script:

```bash
python Iris_Flower_Classification.py
```

5. Enter flower measurements when prompted. Example:

```
Sepal Length (cm): 5.1
Sepal Width (cm): 3.5
Petal Length (cm): 1.4
Petal Width (cm): 0.2
```

Output:

```
🌸 Predicted Iris Species: setosa
```

---

## Conclusion

* KNN effectively classifies Iris flowers based on sepal and petal dimensions
* The model achieves high accuracy (>95%) with `k=3`
* Users can easily predict species by entering custom measurements
* Demonstrates supervised learning, data preprocessing, and interactive prediction using Python

---
