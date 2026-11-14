from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. The Data (Text messages)
# 0 = Normal message (Ham), 1 = Spam
messages = [
    "Win a free iPhone now",
    "Hey, are we still meeting for lunch?",
    "Congratulations! You won a cash prize",
    "Please send me the report by tonight",
    "Claim your free tickets today",
    "Can you pick up some milk on your way home?",
    "URGENT: Your account has been suspended"
]
labels = [1, 0, 1, 0, 1, 0, 1]

# 2. Convert Text to Numbers (Vectorization)
# CountVectorizer turns words into a matrix of numbers based on word frequency
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

print("--- The AI sees the text as numbers! ---")
print(X.toarray()) 
print("Words it learned:", vectorizer.get_feature_names_out())

# 3. Train the Model
# Multinomial Naive Bayes is a classic algorithm for text classification
model = MultinomialNB()
model.fit(X, labels)

# 4. Test it on a brand new message
new_message = ["You have won a free ticket! Claim it now."]
new_X = vectorizer.transform(new_message)
prediction = model.predict(new_X)[0]

print("\n--- Prediction ---")
print(f"New Message: '{new_message[0]}'")

if prediction == 1:
    print("Result: SPAM! 🚨")
else:
    print("Result: Normal Message 📩")