import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def log_error(message):
    """Logs error messages to a file."""
    with open("error_logs.txt", "a") as log_file:
        log_file.write(f"{message}\n")


# 1. Text Generation
def generate_text(prompt):
    """
    Generates text based on a given prompt using the Groq Llama model.
    """

    try:
        # Get the API key from the environment variables
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("API key is missing. Please check your .env file.")

        # Set up the Groq client with the API key
        client = Groq(api_key=api_key)


        # Send a chat completion request
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama3-8b-8192",  # Groq model ID
        )

        # Return the content of the first choice
        return chat_completion.choices[0].message.content

    except Exception as e:
        error_message = f"Error during summarization: {e}"
        log_error(error_message)
        return error_message
