# 1. LISTS (Ordered collections of items)
# Imagine this is a list of AI model scores
model_scores = [85, 92, 78, 95, 88]
print("All scores:", model_scores)

# You can add to a list
model_scores.append(100)
print("After adding a new score:", model_scores)


# 2. DICTIONARIES (Key-Value pairs)
# Imagine this is a user's profile data
user_profile = {
    "name": "Yisa",
    "role": "AI Engineer",
    "skills": ["Python", "Cloud"],
    "is_active": True
}

print("\nUser Name:", user_profile["name"])
print("User Skills:", user_profile["skills"])


# 3. LOOPS (Doing things automatically)
# Let's calculate the average score using a loop
total_score = 0

for score in model_scores:
    total_score = total_score + score

average = total_score / len(model_scores)
print("\nAverage Model Score:", average)

# 4. LOOPING THROUGH A DICTIONARY
print("\n--- Iterating through user data ---")
for key, value in user_profile.items():
    print(f"{key}: {value}")
    # 5. MY CHALLENGE: Find the highest score
highest_score = 0

for score in model_scores:
    if score > highest_score:
        highest_score = score

print("The highest score is:", highest_score)