import random

questions = [
    {
        "question": "What is the capital of Kenya?",
        "options": ["Mombasa", "Nairobi", "Kisumu", "Nakuru"],
        "answer": "nairobi"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    {
        "question": "Who developed Python?",
        "options": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"],
        "answer": "guido van rossum"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    options = q["options"]
    random.shuffle(options)  # shuffle options
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choice = input("Enter the option number: ")
    
    if options[int(choice) - 1].lower() == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer'].title()}\n")

print(f"Your final score is {score}/{len(questions)} 🎉")
# Simple Quiz Game with Multiple Choice Options
