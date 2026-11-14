from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier  # MLP = Multi-Layer Perceptron (Neural Network)
from sklearn.metrics import accuracy_score

# 1. Load the same flower data from Day 11
iris = load_iris()
X = iris.data
y = iris.target

# 2. Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Create the Neural Network!
# hidden_layer_sizes=(10, 10) means 2 hidden layers, with 10 neurons each.
# max_iter=1000 means it will study the data 1000 times to learn.
nn_model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=42)

# 4. Train the "Brain"
print("Training the Neural Network... (this might take 2-3 seconds)")
nn_model.fit(X_train, y_train)

# 5. Test the model
predictions = nn_model.predict(X_test)

# 6. Evaluate
accuracy = accuracy_score(y_test, predictions)
print(f"\nNeural Network Accuracy: {accuracy * 100:.2f}%")

# 7. Make a prediction on a brand new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = nn_model.predict(new_flower)[0]
print(f"New flower prediction: {iris.target_names[prediction]}")