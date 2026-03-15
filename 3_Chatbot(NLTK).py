import nltk
from nltk.tokenize import word_tokenize
import random

print("Hello! I am SmartBot 🤖")
print("Type 'bye' to exit.")

greet_inputs = ["hello", "hi", "hey"]
greet_responses = ["Hello!", "Hi there!", "Hey!"]

responses = {
    "name": "My name is SmartBot.",
    "ai": "AI means Artificial Intelligence.",
    "python": "Python is a popular programming language.",
    "course": "You are studying Computer Science Engineering."
}

while True:

    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye!")
        break

    words = word_tokenize(user_input)

    # Greeting detection
    if any(word in greet_inputs for word in words):
        print("Bot:", random.choice(greet_responses))
        continue

    # Keyword detection
    found = False

    for word in words:
        if word in responses:
            print("Bot:", responses[word])
            found = True
            break

    if not found:
        print("Bot: Sorry, I didn't understand that.")