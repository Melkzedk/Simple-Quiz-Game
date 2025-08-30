# Simple Quiz Game

questions = {
    "What is the capital of Kenya? ": "nairobi",
    "What is 5 + 7? ": "12",
    "Who developed Python? ": "guido van rossum"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question).lower()
    if user_answer == answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {answer}\n")

print(f"Your final score is {score}/{len(questions)} 🎉")
