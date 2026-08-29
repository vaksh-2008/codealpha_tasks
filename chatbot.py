def chatbot():
    print("================================")
    print("       BASIC CHATBOT")
    print("================================")
    print("Type 'bye' to exit the chatbot.")

    while True:
        user_input = input("\nYou: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()