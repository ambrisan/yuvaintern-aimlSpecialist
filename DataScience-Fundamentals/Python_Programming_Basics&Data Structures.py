# 1. Variables and Data Types
age = 20                # Integer (Numerical)
temperature = 98.6      # Float (Numerical)
name = "AI Intern"      # String (Text)
is_active = True        # Boolean (Categorical)

# 2. Data Structures
# List: Mutable, ordered sequence
tech_stack = ["Python", "Pandas", "NumPy"]
tech_stack.append("Scikit-learn")

# Tuple: Immutable, ordered sequence
coordinates = (10.5, -20.3)

# Dictionary: Key-value pairs
student_info = {
    "name": "Ambrisan",
    "major": "AI & DS",
    "semester": 5
}

# Set: Unordered collection of unique items
unique_ids = {101, 102, 103, 101} # Will store as {101, 102, 103}

# 3. Functions, Conditionals, and Loops
def evaluate_performance(score):
    """Categorizes a score using conditionals."""
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    else:
        return "Needs Improvement"

# Loop through a list and apply the function
scores = [95, 82, 60]
print("--- Performance Evaluation ---")
for s in scores:
    print(f"Score: {s} -> {evaluate_performance(s)}")