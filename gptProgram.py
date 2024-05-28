import openai

# Set your OpenAI API key
openai.api_key = 'CHANGE_TO_YOUR_KEY'  # Replace with your actual API key

def get_command_explanation(command):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use "gpt-4" or "gpt-3.5-turbo" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Explain the following Linux command: {command}"}
            ],
            max_tokens=65  # Adjust this as needed
        )
        explanation = response['choices'][0]['message']['content'].strip()
        return explanation
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"

def main():
    while True:
        command = input("Enter a Linux command (or 'exit' to quit): ")
        if command.lower() == 'exit':
            break
        explanation = get_command_explanation(command)
        print(f"\nExplanation for '{command}':\n{explanation}\n")

if __name__ == "__main__":
    main()
