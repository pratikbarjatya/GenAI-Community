import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Cookie Policy | AI News Generator",
    page_icon="🍪",
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
    st.markdown("<h1 style='font-size: 60px; text-align: center;'>Cookie Policy</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: gray; text-align: center;'>Learn how and why we use cookies to enhance your experience on our platform. 🍪</p>", unsafe_allow_html=True)

    # Accordion-Like Cookie Policy Sections
    st.markdown("<h2 style='font-size: 30px; margin-top: 30px;'>Cookie Policy Details</h2>", unsafe_allow_html=True)

    # Section 1
    with st.expander("🍪 What Are Cookies?"):
        st.write("""
        Cookies are small text files that are stored on your device when you visit a website. 
        They help us understand user behavior, improve functionality, and provide personalized services.
        """)

    # Section 2
    with st.expander("📊 How We Use Cookies"):
        st.write("""
        We use cookies for the following purposes:
        - To remember your preferences and settings.
        - To analyze how you use our platform.
        - To enhance the overall user experience.
        - To ensure the website functions as intended.
        """)

    # Section 3
    with st.expander("🔍 Types of Cookies We Use"):
        st.write("""
        We use the following types of cookies:
        - **Essential Cookies**: Necessary for basic website functionality.
        - **Performance Cookies**: Help us understand website usage and improve its performance.
        - **Functional Cookies**: Store your preferences for a personalized experience.
        - **Analytics and Tracking Cookies**: Monitor user behavior for insights and improvement.
        """)

    # Section 4
    with st.expander("🛡️ Managing Your Cookie Preferences"):
        st.write("""
        You can manage or disable cookies by adjusting your browser settings. 
        However, disabling cookies may limit certain functionalities of our platform.
        """)

    # Section 5
    with st.expander("⚖️ Third-Party Cookies"):
        st.write("""
        Some cookies on our platform may come from third-party services such as analytics or social media providers. 
        We recommend reviewing their cookie policies to understand how they use your data.
        """)

    # Section 6
    with st.expander("📅 Changes to This Cookie Policy"):
        st.write("""
        We may update this cookie policy from time to time. Any changes will be posted on this page, 
        and we encourage you to review it periodically.
        """)

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
