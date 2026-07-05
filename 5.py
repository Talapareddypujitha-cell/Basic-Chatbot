def chatbot():
    print("=" * 40)
    print("      🤖 PYTHON CHATBOT")
    print("=" * 40)
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello" or user == "hi":
            print("Bot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")

        elif user == "what is your name":
            print("Bot: My name is Python ChatBot.")

        elif user == "who created you":
            print("Bot: I was created using Python programming.")

        elif user == "what can you do":
            print("Bot: I can answer simple questions and chat with you.")

        elif user == "python":
            print("Bot: Python is a popular programming language.")

        elif user == "time":
            from datetime import datetime
            print("Bot: Current Time:", datetime.now().strftime("%I:%M:%S %p"))

        elif user == "date":
            from datetime import date
            print("Bot: Today's Date:", date.today())

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()