import random

print("NAMASKER! I am Little SmartBot 🤖")
print("Type 'bye' to exit.")

greetings = ["hello", "hi", "hey"]
greet_responses = ["Namaskar ji!", "what's up buddy!", "Heyyyyyyyyy!"]

questions = {"course": "You are studying Computer Science Engineering.",
    "name": "My name is SmartBot made by Sumit Sir.",
    "ai": "AI means Artificial Intelligence .",
    "python": "Python is a very popular programming language."
}
while True:
    user = input("You: ").lower()# ismai jo bhi user input karega vo lower ho jayegaa

    if user == "bye":
        print("Bot: Goodbye!")
        break

    elif any(word in user for word in greetings):
        print("Bot:", random.choice(greet_responses))

    else:
        found = False
        for key in questions:
            if key in user:
                print("Bot:", questions[key])
                found = True
                break

        if not found:
            print("Bot: Sorry I don't understand that.")            
    