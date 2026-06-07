hile True:
    user = input("You: ").strip().lower()

    if user == "hello":
        print("Bot: Hello!")
    elif user == "how are you":
        print("Bot: I am fine. what about you?")
    elif user == "what is your name":
        print("Bot: I am Python chatbot.")  
    elif user == "help":
        print("Bot: Ask me hello, how are you,name, bye")      
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand. Type 'help' for options.")
