# Initialize the user score
score = 0

print("=== Python Variables Quiz ===")
print("Answer by typing A, B, C, or D.\n")

# --- QUESTION 1 ---
print("Question 1: Which of the following is a VALID variable name in Python?")
print("A) 2_user_name")
print("B) user_name")
print("C) user-name")
print("D) class")

# Get user input and convert to uppercase
answer1 = input("Your answer: ").strip().upper()

if answer1 == "B":
    print("✅ Correct! Variables must start with a letter or underscore.")
    score = score + 1
else:
    print("❌ Incorrect. The correct answer is B. 'A' starts with a number, 'C' contains a hyphen, and 'D' is a reserved keyword.")

print("-" * 40)

# --- QUESTION 2 ---
print("Question 2: Look at this code:\n   x = 10\n   x = 'Apple'\nWhat will print(type(x)) output?")
print("A) <class 'int'>")
print("B) <class 'str'>")
print("C) Error")
print("D) <class 'list'>")

answer2 = input("Your answer: ").strip().upper()

if answer2 == "B":
    print("✅ Correct! Python is dynamically typed; variables can change types seamlessly.")
    score = score + 1
else:
    print("❌ Incorrect. The correct answer is B. The type changed from integer to string.")

print("-" * 40)

# --- QUESTION 3 ---
print("Question 3: How do you assign the value 5 to multiple variables (x, y, and z) at once?")
print("A) x = y = z = 5")
print("B) x, y, z = 5")
print("C) x = 5, y = 5, z = 5")
print("D) x & y & z = 5")

answer3 = input("Your answer: ").strip().upper()

if answer3 == "A":
    print("✅ Correct! Python uses chained assignment to give multiple variables the same value.")
    score = score + 1
else:
    print("❌ Incorrect. The correct answer is A. Option B throws an unpacking error.")

print("-" * 40)

# --- FINAL SCORE ---
print(f"=== Quiz Complete ===")
print(f"Your final score: {score} out of 3")

