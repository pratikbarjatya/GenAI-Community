import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Contact Us | AI News Generator",
    page_icon="📞",
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

    # Include Font Awesome CDN for icons
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

    # Title Section
    st.markdown("<h1 style='font-size: 60px; text-align: center;'>Contact Us</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; text-align: center; color: gray;'>We'd love to hear from you! Reach out with any questions or feedback.</p>", unsafe_allow_html=True)

    # Contact Form
    st.markdown("<h2 style='font-size: 30px;'>📬 Get in Touch</h2>", unsafe_allow_html=True)
    st.write("Fill in the form below to contact us directly!")

    contact_form = st.form(key='contact_form')
    name = contact_form.text_input("Your Name")
    email = contact_form.text_input("Your Email")
    message = contact_form.text_area("Your Message")
    submit_button = contact_form.form_submit_button("Send Message")

    if submit_button:
        if name and email and message:
            st.success("Thank you for reaching out! We will get back to you soon.")
        else:
            st.error("Please fill in all the fields.")

    # Contact Information Section
    st.markdown("<h2 style='font-size: 30px;'>📍 Our Location</h2>", unsafe_allow_html=True)
    st.write("Find us at our office location:")

    st.markdown("""
     <div style='width: 100%; height: 100%;'>
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3426.9461831002777!2d73.43206937626101!3d30.80414347455002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3922a73c3c264d03%3A0x1654eeba796b65a3!2sMohammad%20Ali%20Jinnah%20Rd%2C%20Okara%2C%20Punjab%2C%20Pakistan!5e0!3m2!1sen!2s!4v1733648554209!5m2!1sen!2s" 
        width="100%" height="600" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
     </div>""", unsafe_allow_html=True)

    # Social Media Section
    st.markdown("<h2 style='font-size: 30px;'>💬 Follow Us</h2>", unsafe_allow_html=True)
    st.write("Stay connected with us through social media:")
    social_media_links = {
        "GitHub": "https://github.com/yourprofile",
        "LinkedIn": "https://www.linkedin.com/in/yourprofile",
        "Twitter": "https://twitter.com/yourprofile"
    }

    for platform, link in social_media_links.items():
        st.markdown(f"""
        <a href='{link}' target='_blank' style='font-size: 20px; color: #0077B5; margin-right: 20px;'>
            <i class="fab fa-{platform.lower()}" style="font-size: 24px;"></i> {platform}
        </a>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
        unsafe_allow_html=True
    )

# Run the app
if __name__ == "__main__":
    main()
