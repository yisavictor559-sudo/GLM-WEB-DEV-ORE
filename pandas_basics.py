import pandas as pd

# 1. Create a simple dataset (like an Excel table)
data = {
    "Model_Name": ["GPT-4", "Claude 3", "Llama 3", "Gemini"],
    "Accuracy_Score": [95, 93, 88, 91],
    "Cost_Per_1k_Tokens": [0.03, 0.02, 0.00, 0.01] # Llama is free/open-source!
}

# 2. Load the data into a Pandas DataFrame
df = pd.DataFrame(data)

# 3. Look at the data!
print("--- Full DataFrame ---")
print(df)

# 4. Basic Data Analysis
print("\n--- Basic Statistics ---")
print("Average Accuracy:", df["Accuracy_Score"].mean())

# 5. Filtering Data (Super important for AI)
print("\n--- Models with Accuracy > 90 ---")
high_accuracy_models = df[df["Accuracy_Score"] > 90]
print(high_accuracy_models)
# 6. MY CHALLENGE: Find the lowest cost
print("\n--- Cheapest Model ---")
cheapest_model = df[df["Cost_Per_1k_Tokens"] == df["Cost_Per_1k_Tokens"].min()]
print(cheapest_model)