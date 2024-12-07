from user_input import get_user_inputs
from news_retrieval import fetch_news
from summarization import summarize_text
import streamlit as st


def log_error(message):
    """Logs error messages to a file."""
    with open("error_logs.txt", "a") as log_file:
        log_file.write(f"{message}\n")


def main():
    try:
        # Step 1: User Input Section
        user_inputs = get_user_inputs()

        # Proceed only if inputs are submitted
        if user_inputs:
            st.write("Inputs received:")
            st.write(user_inputs)

            # Step 2: News Retrieval Section
            st.subheader("Fetching News Articles...")
            news_articles = fetch_news(user_inputs["prompt"])

            # Display and summarize news articles
            if news_articles:
                st.write("News Articles Retrieved:")
                for idx, article in enumerate(news_articles):
                    if "error" in article:
                        st.error(article["error"])
                        log_error(article["error"])  # Log the error
                    else:
                        st.write(f"- **{article['title']}** (Source: {article['source']})")
                        st.write(f"  Description: {article['description']}")
                        st.write(f"  [Read More]({article['url']})")

                        # Step 3: Summarization Section
                        st.subheader(f"Summary for Article {idx + 1}:")
                        summary = summarize_text(article['description'], user_inputs["tone"])
                        st.write(summary)

    except Exception as e:
        error_message = f"An unexpected error occurred in the main function: {e}"
        log_error(error_message)
        st.error(error_message)


if __name__ == "__main__":
    main()
