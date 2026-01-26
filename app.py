def chatbot():
    print("Hello! This is my first chatbot.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        print("Bot:", user_input)


if __name__ == "__main__":
    chatbot()
