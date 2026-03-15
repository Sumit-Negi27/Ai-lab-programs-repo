#Ye chatbot if-else logic se kaam karta hai. Matlab user jo word likhega uske according bot answer dega.

print("NAMASKAR! I am a simplest chatbot.")
print("Type 'end' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How are you?")
    elif user == "hey":
        print("Bot:helloo ji!")
    elif user == "hi":
        print("Bot: hello bro!")
    elif user == "yoo":
        print("Bot: whatsup buddy!")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")
    
    elif user == "what is your name":
        print("Bot: I am a simple chatbot made by Sumit Sir.")
    elif user == "what is ai":
        print("Bot: AI means Artificial Intelligence.")
    elif user == "end":
        print("Bot: okay Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")