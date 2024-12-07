import streamlit as st


def get_user_inputs():
    # Title
    st.title("AI-Driven Daily News Content Generator")

    # Input fields
    st.subheader("User Input")
    prompt = st.text_input("Enter your prompt:", placeholder="E.g., 'Create a funny post about AI replacing jobs.'")
    tone = st.selectbox("Select Tone:", ["Humorous", "Formal", "Conversational"])
    platform = st.selectbox("Select Platform:", ["LinkedIn", "Instagram", "Twitter"])
    output_format = st.multiselect("Choose Output Format(s):", ["Text", "Image", "Video", "Meme"])

    # Button to submit
    if st.button("Submit"):
        # Return inputs as a dictionary
        return {
            "prompt": prompt,
            "tone": tone,
            "platform": platform,
            "output_format": output_format
        }
    return None
