import os
from groq import Groq

def log_error(message):
    """Logs error messages to a file."""
    with open("error_logs.txt", "a") as log_file:
        log_file.write(f"{message}\n")

def summarize_text(text, tone):
    """Uses Groq's chat completion API to summarize text."""
    try:
        # Set up the Groq client with your API key
        client = Groq(api_key="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")

        # Construct the prompt for summarization
        prompt = f"Summarize the following text in a {tone.lower()} tone:\n\n{text}"

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
