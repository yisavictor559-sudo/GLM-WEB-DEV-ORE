import joblib
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# 1. Load the data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Train the model
model = DecisionTreeClassifier()
model.fit(X, y)
print("Model trained successfully!")

# 3. Save the model to a file!
joblib.dump(model, 'iris_model.pkl')
print("Model saved to 'iris_model.pkl'!")