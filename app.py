conversation_history = []


def build_prompt(user_input):
    """
    Builds a structured prompt using conversation memory.
    """
    system_instruction = (
        "You are a helpful AI assistant. "
        "Use the conversation history to answer naturally."
    )

    history_text = ""
    for message in conversation_history:
        history_text += f"{message['role']}: {message['content']}\n"

    prompt = (
        f"{system_instruction}\n\n"
        f"{history_text}"
        f"User: {user_input}\n"
        f"Assistant:"
    )

    return prompt


def generate_ai_response(prompt):
    """
    Placeholder for AI model call.
    This will later be replaced with AWS Bedrock.
    """
    return "This is a simulated AI response using conversation memory."


def chatbot():
    print("AI Agent started. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        conversation_history.append(
            {"role": "User", "content": user_input}
        )

        prompt = build_prompt(user_input)
        response = generate_ai_response(prompt)

        conversation_history.append(
            {"role": "Assistant", "content": response}
        )

        print("Bot:", response)


if __name__ == "__main__":
    chatbot()
