import random

# Define the questions and answers
questions = [
    {"question": "What is the capital of France?", "options": ["A) Paris", "B) Rome", "C) Madrid", "D) Berlin"], "answer": "A"},
    {"question": "What is 2 + 2?", "options": ["A) 3", "B) 4", "C) 5", "D) 6"], "answer": "B"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"], "answer": "B"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["A) Harper Lee", "B) J.K. Rowling", "C) Ernest Hemingway", "D) Mark Twain"], "answer": "A"},
    {"question": "What is the square root of 64?", "options": ["A) 6", "B) 7", "C) 8", "D) 9"], "answer": "C"},
    {"question": "Who painted the Mona Lisa?", "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"], "answer": "C"},
]

# Define prize money for each level
prizes = [100, 200, 300, 500, 1000, 2000]

# Function to ask questions
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    return answer == question_data["answer"]

def play_game():
    correct_answers = 0
    for i, question in enumerate(questions):
        if ask_question(question):
            print("Correct!")
            correct_answers += 1
            print(f"Your prize money: ${prizes[correct_answers - 1]}")
        else:
            print("Incorrect. Game over.")
            break

    if correct_answers == len(questions):
        print(f"Congratulations! You've won the top prize of ${prizes[-1]}!")
    else:
        print(f"Game over. You've won a total of ${prizes[correct_answers - 1]}!")

# Start the game
play_game()
