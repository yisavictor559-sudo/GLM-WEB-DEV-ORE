from flask import Flask, request, jsonify ,render_template
from sklearn.tree import DecisionTreeClassifier

# 1. Setup the Web App
app = Flask(__name__)

# 2. Train the AI Model
X = [[25, 10], [45, 5], [35, 15], [20, 2], [50, 20]]
y = [0, 0, 1, 0, 1]
model = DecisionTreeClassifier()
model.fit(X, y)

# 3. Create an API Endpoint (The "Waiter")
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():
    # Get the age and time from the URL
    age = int(request.args.get('age'))
    time = int(request.args.get('time'))
    
    # Make the prediction
    prediction = model.predict([[age, time]])[0]
    
    # Return the answer as JSON (the universal language of the web)
    return jsonify({
        "status": "success",
        "input_age": age,
        "input_time": time,
        "prediction": int(prediction),
        "message": "Will click the ad!" if prediction == 1 else "Will NOT click."
    })

# 4. Run the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)