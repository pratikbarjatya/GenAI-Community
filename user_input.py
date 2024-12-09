import streamlit as st

def get_user_inputs():
    # Title
    st.title("AI-Driven Content Generator")

    # Input fields
    st.subheader("User Input")
    prompt = st.text_input(
        "Enter your prompt:",
        placeholder="E.g., 'Generate a meme about AI replacing jobs.'"
    )

    platform = st.selectbox(
        "Select Platform:",
        ["LinkedIn", "Instagram", "Twitter", "General"]
    )

    output_format = st.multiselect(
        "Choose Output Format(s):",
        ["Text", "Image", "Video", "Meme"],
        help="Select the type of content you'd like to generate."
    )

    # Input validation
    if not prompt:
        st.warning("Please enter a prompt to proceed.")

    # Button to submit inputs
    if st.button("Submit"):
        if prompt and output_format:
            # Return inputs as a dictionary
            return {
                "prompt": prompt,
                "platform": platform,
                "output_format": output_format
            }
        else:
            st.error("Please provide a valid prompt and select at least one output format.")
    
    return None
