import os
from user_input import get_user_inputs
from news_retrieval import fetch_news
from summarization import summarize_text
from text_generation import generate_text
import streamlit as st
import requests
from dotenv import load_dotenv

# Page Configuration
st.set_page_config(
    page_title="Home | AI News Generator",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <head>
        <meta property="og:title" content="Home | AI News Generator" />
        <meta property="og:description" content="Empowering you to stay ahead with AI-curated, real-time news from around the globe. Experience the future of content generation, tailored just for you!" />
        <meta property="og:image" content="logo.png" />
        <meta property="og:type" content="website" />
    </head>
""", unsafe_allow_html=True)

# Load environment variables from .env file
load_dotenv()

# Utility: Log Errors
def log_error(message):
    """Logs error messages to a file."""
    with open("error_logs.txt", "a") as log_file:
        log_file.write(f"{message}\n")

# Utility: Detect Tone
def detect_tone(prompt):
    """Detects the tone of the prompt using Hugging Face API."""
    try:
        api_url = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
        api_key = os.getenv("HUGGING_FACE_API")
        if not api_key:
            raise ValueError("Hugging Face API key is missing. Please check your .env file.")

        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.post(api_url, headers=headers, json={"inputs": prompt})
        response.raise_for_status()

        predictions = response.json()
        if isinstance(predictions, list) and predictions:
            label_mapping = {
                'LABEL_0': "Negative",
                'LABEL_1': "Neutral",
                'LABEL_2': "Positive"
            }
            top_prediction = max(predictions[0], key=lambda x: x["score"])
            return label_mapping.get(top_prediction["label"], "Unknown tone")
        else:
            return "Unknown tone"

    except Exception as e:
        log_error(f"Error detecting tone: {e}")
        return "Tone detection failed"

# Main Function
def main():
    # Apply Custom Font
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    html, body, [class*="css"], *{
        font-family: 'Poppins', sans-serif;
    }
    </style>""", unsafe_allow_html=True)

    # Title and Logo Section
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<h1 style='font-size: 60px; margin-top: 20px;'>AI DRIVEN DAILY NEWS CONTENT GENERATOR</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 20px; color: gray;'>Empowering you to stay ahead with AI-curated, real-time news from around the globe. Experience the future of content generation, tailored just for you!</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 20px; color: gray;'>Your trusted partner for reliable, dynamic, and innovative news solutions. 🚀🤝</p>", unsafe_allow_html=True)
        st.markdown("""
        <ul style='font-size: 18px; color: gray;'>
            <li>🌟 Generate news articles in seconds.</li>
            <li>🧠 Powered by cutting-edge AI algorithms.</li>
            <li>🌍 Covering global events with precision.</li>
            <li>📡 Designed for journalists, students, and professionals alike.</li>
        </ul>
        """, unsafe_allow_html=True)
    with col2:
        st.image("logo.png", width=600)

    try:
        # Step 1: User Input Section
        user_inputs = get_user_inputs()

        if user_inputs:
            st.write("Inputs received:")
            st.write(user_inputs)

            # Step 2: Detect Tone
            st.subheader("Detected Tone")
            tone = detect_tone(user_inputs["prompt"])
            st.info(f"Detected Tone: {tone}")

            # Step 3: News Retrieval
            st.subheader("Fetching News Articles...")
            news_articles = fetch_news(user_inputs["prompt"])

            if news_articles:
                st.write("News Articles Retrieved:")
                for idx, article in enumerate(news_articles):
                    if "error" in article:
                        st.error(article["error"])
                        log_error(article["error"])
                    else:
                        st.write(f"- **{article['title']}** (Source: {article['source']})")
                        st.write(f"  Description: {article['description']}")
                        st.write(f"  [Read More]({article['url']})")

                        # Step 4: Summarization
                        st.subheader(f"Summary for Article {idx + 1}:")
                        summary = summarize_text(article['description'], tone)
                        st.write(summary)

            # Step 5: Text Generation
            st.subheader("Text Generated from Prompt")
            generated_text = generate_text(user_inputs["prompt"])
            st.write(generated_text)

            # Step 6: Handle Multiple Output Formats
            if len(user_inputs["output_format"]) > 1:
                st.markdown('<p style="color: red; font-size: 16px; font-weight: bold;">⚠️ Due to limited resources, only Text generation and News Retrieval are supported.</p>',
                unsafe_allow_html=True)
            elif "Text" in user_inputs["output_format"]:
                st.write("Text generation completed successfully.")
            else:
                st.markdown('<p style="color: red; font-size: 16px; font-weight: bold;">⚠️ No supported formats selected.</p>',
                unsafe_allow_html=True)

    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        log_error(error_message)
        st.error(error_message)

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
        unsafe_allow_html=True
    )

    st.sidebar.success("Select a page above.")

# Run the Application
if __name__ == "__main__":
    main()


# import os
# from user_input import get_user_inputs
# from news_retrieval import fetch_news
# from summarization import summarize_text
# from text_generation import generate_text
# import streamlit as st
# import requests
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# def log_error(message):
#     """Logs error messages to a file."""
#     with open("error_logs.txt", "a") as log_file:
#         log_file.write(f"{message}\n")

# def detect_tone(prompt):
#     """Detects the tone of the prompt using Hugging Face API."""
#     try:
#         # Hugging Face Inference API endpoint
#         api_url = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
        
#         # Your Hugging Face API key (set as environment variable or replace below)
#         api_key = os.getenv("HUGGING_FACE_API")
#         if not api_key:
#             raise ValueError("Hugging Face API key is missing. Please check your .env file.")

#         # Set the request headers
#         headers = {"Authorization": f"Bearer {api_key}"}
        
#         # Send the request to the Hugging Face API
#         response = requests.post(api_url, headers=headers, json={"inputs": prompt})
#         response.raise_for_status()
        
#         # Parse the response
#         predictions = response.json()
#         if isinstance(predictions, list) and predictions:
            
#             # Mapping of labels to human-readable tones
#             label_mapping = {
#                 'LABEL_0': "Negative",
#                 'LABEL_1': "Neutral",
#                 'LABEL_2': "Positive"
#             }
#             top_prediction = max(predictions[0], key=lambda x: x["score"])
#             tone_label = label_mapping.get(top_prediction["label"], "Unknown tone")
#             return tone_label
#         else:
#             return "Unknown tone"

#     except Exception as e:
#         log_error(f"Error detecting tone: {e}")
#         return "Tone detection failed"

# def main():
#     try:
#         # Step 1: User Input Section
#         user_inputs = get_user_inputs()

#         # Proceed only if inputs are submitted
#         if user_inputs:
#             st.write("Inputs received:")
#             st.write(user_inputs)

#             # Step 2: Detect Tone
#             st.subheader("Detected Tone")
#             tone = detect_tone(user_inputs["prompt"])
#             st.info(f"Detected Tone: {tone}")

#             # Step 3: News Retrieval Section
#             st.subheader("Fetching News Articles...")
#             news_articles = fetch_news(user_inputs["prompt"])

#             # Display and summarize news articles
#             if news_articles:
#                 st.write("News Articles Retrieved:")
#                 for idx, article in enumerate(news_articles):
#                     if "error" in article:
#                         st.error(article["error"])
#                         log_error(article["error"])  # Log the error
#                     else:
#                         st.write(f"- **{article['title']}** (Source: {article['source']})")
#                         st.write(f"  Description: {article['description']}")
#                         st.write(f"  [Read More]({article['url']})")

#                         # Step 4: Summarization Section
#                         st.subheader(f"Summary for Article {idx + 1}:")
#                         summary = summarize_text(article['description'], tone)
#                         st.write(summary)
#            # Step 4: Text Generation Section
#             st.subheader("Text Generated from Prompt")
#             generated_text = generate_text(user_inputs["prompt"])
#             st.write(generated_text)

#             # Step 5: Handle Multiple Output Formats
#             if len(user_inputs["output_format"]) > 1:
#                 st.warning("Due to limited resources, only Text generation and News Retrieval are supported.")
#             elif "Text" in user_inputs["output_format"]:
#                 st.write("Text generation completed successfully.")
#             else:
#                 st.warning("No supported formats selected.")    

#     except Exception as e:
#         error_message = f"An unexpected error occurred in the main function: {e}"
#         log_error(error_message)
#         st.error(error_message)

# # Run App
# if __name__ == "__main__":
#     main()
