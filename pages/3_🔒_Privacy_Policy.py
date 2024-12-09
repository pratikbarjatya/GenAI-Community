import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Privacy Policy | AI News Generator",
    page_icon="🔒",
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
    st.markdown("<h1 style='font-size: 60px; text-align: center;'>Privacy Policy</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: gray; text-align: center;'>Your data security and privacy matter to us. Learn how we collect, use, and protect your information. 🔒</p>", unsafe_allow_html=True)

    # Accordion-Like Privacy Sections
    st.markdown("<h2 style='font-size: 30px; margin-top: 30px;'>Privacy Policy Details</h2>", unsafe_allow_html=True)

    # Section 1
    with st.expander("🔍 Information We Collect"):
        st.write("""
        We collect the following types of information to provide and improve our services:
        - Personal information you provide (e.g., name, email, preferences).
        - Usage data, such as the actions you take while using our site.
        - Technical information, including browser type and IP address.
        """)

    # Section 2
    with st.expander("📊 How We Use Your Information"):
        st.write("""
        We use the collected information for the following purposes:
        - To provide, maintain, and improve our services.
        - To personalize user experience.
        - To communicate updates, newsletters, and relevant notifications.
        """)

    # Section 3
    with st.expander("🛡️ How We Protect Your Information"):
        st.write("""
        We prioritize the security of your data by:
        - Implementing secure communication protocols (e.g., HTTPS).
        - Regularly updating and maintaining system security.
        - Ensuring data encryption and access restrictions.
        """)

    # Section 4
    with st.expander("📤 Sharing Your Information"):
        st.write("""
        We do not sell, trade, or rent your personal information. However, we may share your data:
        - With service providers assisting in app functionality.
        - If required by law or to protect our rights.
        """)

    # Section 5
    with st.expander("⚖️ Your Rights"):
        st.write("""
        You have the right to:
        - Access and download your personal data.
        - Request data correction or deletion.
        - Opt-out of promotional communications.
        """)

    # Section 6
    with st.expander("🌍 Third-Party Services"):
        st.write("""
        Our app may link to third-party services, which have their own privacy policies. We recommend reviewing their policies before sharing any information.
        """)

    # Section 7
    with st.expander("📅 Updates to This Privacy Policy"):
        st.write("""
        This privacy policy may be updated occasionally. We encourage you to check this page regularly for updates. Any changes will be effective immediately upon posting.
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
