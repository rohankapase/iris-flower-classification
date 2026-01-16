import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
iris = pd.read_csv(r"D:\PROJECT\Iris Flower Classification\Iris.csv")

# Make column names lowercase
iris.columns = iris.columns.str.lower()

# Drop id column
X = iris.drop(["id", "species"], axis=1)
y = iris["species"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)


# Train KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

print("Model trained successfully ✅")
print("Accuracy:", knn.score(X_test, y_test))

# USER INPUT SECTION
print("\nEnter Iris Flower Measurements:")

sepal_length = float(input("Sepal Length (cm): "))
sepal_width = float(input("Sepal Width (cm): "))
petal_length = float(input("Petal Length (cm): "))
petal_width = float(input("Petal Width (cm): "))

# Convert input to DataFrame (IMPORTANT)
X_new = pd.DataFrame(
    [[sepal_length, sepal_width, petal_length, petal_width]],
    columns=X.columns
)

# Prediction
prediction = knn.predict(X_new)
print("\n🌸 Predicted Iris Species:", prediction[0])
