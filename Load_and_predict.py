import joblib

# 1. Load the saved model file
print("Loading the model...")
model = joblib.load('iris_model.pkl')
print("Model loaded instantly!")

# 2. Make a prediction on a new flower
new_flower = [[5.9, 3.0, 5.1, 1.8]] # This looks like a bigger flower
prediction = model.predict(new_flower)[0]

# 3. Print the result
flower_names = ['Setosa', 'Versicolor', 'Virginica']
print(f"\nPrediction for new flower: {flower_names[prediction]}")