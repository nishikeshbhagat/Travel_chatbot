import aiml

# Create an empty kernel
kernel = aiml.Kernel()

# Load the AIML file
aiml_path = "travel.aiml"
kernel.learn(aiml_path)

# Initialize a variable to track the conversation state
conversation_state = None

# Main loop
while True:
    # Get user input
    user_input = input("You: ")

    # Quit if user enters "quit"
    if user_input.lower() == 'quit':
        break

    # Get bot response
    bot_response = kernel.respond(user_input)

    # Print bot response
    print("Chatbot:", bot_response)
