import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="FAQs | AI News Generator",
    page_icon="❓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Main Function
def main():
    # Apply Poppins font across the app
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    html, body, [class*="css"], * {
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title Section
    st.markdown("<h1 style='font-size: 60px; text-align: center;'>Frequently Asked Questions</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; text-align: center; color: gray;'>Here are some of the most commonly asked questions. If you have more questions, feel free to contact us! 📨</p>", unsafe_allow_html=True)

    # FAQ Section 1: General Questions
    st.markdown("<h2 style='font-size: 40px;'>🌐 General Questions</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 30px;'>Q1: What is AI News Generator?</h3>", unsafe_allow_html=True)
    st.write("**AI News Generator** is an innovative tool powered by Generative AI that creates personalized, real-time news content for individuals and organizations. We aim to revolutionize the news industry with faster, smarter, and more accessible news creation.")

    st.markdown("<h3 style='font-size: 30px;'>Q2: How does AI News Generator work?</h3>", unsafe_allow_html=True)
    st.write("Our AI model leverages advanced **Natural Language Processing (NLP)** and **Generative AI** techniques to generate relevant and personalized news articles based on various data sources. It offers real-time news updates for better engagement and accessibility.")

    # FAQ Section 2: Technical Questions
    st.markdown("<h2 style='font-size: 40px;'>🛠️ Technical Questions</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 30px;'>Q3: What technology stack does AI News Generator use?</h3>", unsafe_allow_html=True)
    st.write("""
    Our application uses the following technologies:
    - **Generative AI models** to generate news content
    - **Streamlit** for the user interface
    - **Python Libraries** for backend integration
    - **Open-source APIs** to keep the app efficient and cost-effective
    """)

    st.markdown("<h3 style='font-size: 30px;'>Q4: Is AI News Generator free to use?</h3>", unsafe_allow_html=True)
    st.write("Yes! **AI News Generator** is completely free to use. We use free resources and open-source models to provide accessible news creation for everyone.")

    # FAQ Section 3: Privacy and Security
    st.markdown("<h2 style='font-size: 40px;'>🔐 Privacy & Security</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 30px;'>Q5: How is my data handled?</h3>", unsafe_allow_html=True)
    st.write("""
    Your privacy is important to us. We only collect data required to generate news content and improve your experience. 
    We do not share or sell any personal data, and all data processing is in compliance with our **Privacy Policy**.
    """)

    st.markdown("<h3 style='font-size: 30px;'>Q6: Is my personal information secure?</h3>", unsafe_allow_html=True)
    st.write("Yes, we ensure that your personal information is encrypted and stored securely. We follow the best practices in cybersecurity to protect your data.")

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
        unsafe_allow_html=True
    )
    st.sidebar.success("Select a page above.")

# Run the app
if __name__ == "__main__":
    main()
