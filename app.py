def build_prompt(user_input):
    """
    Builds a structured prompt for the AI model.
    """
    system_instruction = (
        "You are a helpful AI assistant. "
        "Answer clearly and concisely."
    )

    prompt = f"{system_instruction}\nUser: {user_input}\nAssistant:"
    return prompt


def generate_ai_response(prompt):
    """
    Placeholder for AI model call.
    This will later be replaced with AWS Bedrock.
    """
    return "This is a simulated AI response based on the prompt."


def chatbot():
    print("AI Chatbot started. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        prompt = build_prompt(user_input)
        response = generate_ai_response(prompt)

        print("Bot:", response)


if __name__ == "__main__":
    chatbot()
