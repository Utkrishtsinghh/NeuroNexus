def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm an AI, but I'm doing great! How about you?"
    elif "what can you do" in user_input:
        return "I can chat with you and make your day better!"
    elif "what is neuronexus" in user_input or "tell me about neuronexus" in user_input:
        return "NeuroNexus is a company that specializes in advanced neural technologies. They are known for making commercial silicon probes - tiny devices used to record electrical activity from the brain."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day ahead!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    print("Welcome to NeuroNexus Chatbot! (Type 'bye' to exit)\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break

if __name__ == "__main__":
    main()
