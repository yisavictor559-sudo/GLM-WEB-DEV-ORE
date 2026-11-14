from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Load a real-world dataset (Iris Flowers)
# It has 150 rows of data (sepal length, sepal width, etc.) to predict the flower type.
iris = load_iris()
X = iris.data   # The features (measurements)
y = iris.target # The labels (flower types: 0, 1, or 2)

print(f"Total rows of data: {len(X)}")

# 2. Split the data: 80% for training, 20% for testing
# random_state=42 just means "shuffle the data the same way every time"
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training rows: {len(X_train)}")
print(f"Testing rows: {len(X_test)}")

# 3. Create and Train the Model (ONLY on the training data!)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 4. Test the model on the 20% of data it has NEVER seen
predictions = model.predict(X_test)

# 5. Calculate the Accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# 6. Make a prediction for a brand new flower
# (Sepal Length: 5.1, Sepal Width: 3.5, Petal Length: 1.4, Petal Width: 0.2)
new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_flower)[0]

print(f"\nNew flower prediction: {prediction}")
print(f"Meaning: This is a {iris.target_names[prediction]}")