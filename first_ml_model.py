from sklearn.tree import DecisionTreeClassifier

# 1. The Data (Features)
# Imagine we are predicting if a user will click an ad based on their age and time on site.
# [Age, Minutes_On_Site]
X = [
    [25, 10],  # User 1
    [45, 5],   # User 2
    [35, 15],  # User 3
    [20, 2],   # User 4
    [50, 20],  # User 5
]

# 2. The Answers (Labels)
# 0 = Didn't click, 1 = Clicked
y = [0, 0, 1, 0, 1]

# 3. Create the Model (We are using a Decision Tree)
model = DecisionTreeClassifier()

# 4. Train the Model (This is where the "AI" happens)
model.fit(X, y)
print("Model trained successfully!")

# 5. Make a Prediction for a NEW user
# Let's test a 30-year-old who spent 12 minutes on the site
new_user = [[50, 25]]
prediction = model.predict(new_user)

print(f"Prediction for new user [Age 30, 12 mins]: {prediction[0]}")

if prediction[0] == 1:
    print("The AI predicts this user WILL click the ad! 🎯")
else:
    print("The AI predicts this user will NOT click the ad. 🙅‍♂️")