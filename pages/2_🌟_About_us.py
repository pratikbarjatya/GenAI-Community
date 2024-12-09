import streamlit as st
import os  # Missing import added

# Set page configuration
st.set_page_config(
    page_title="About Us | AI News Generator",
    page_icon="🌟",
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

    # Add Font Awesome CDN for icons
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    """, unsafe_allow_html=True)

    # Title Section
    st.markdown("<h1 style='font-size: 60px; text-align: center;'>About Us</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; text-align: center; color: gray;'>Learn more about the vision, mission, and team behind the AI News Generator. 🌍📰</p>", unsafe_allow_html=True)

    # Section 1: Our Vision
    st.markdown("<h2 style='font-size: 30px;'>🌟 Our Vision</h2>", unsafe_allow_html=True)
    st.write("""
    At **AI News Generator**, we aim to revolutionize the way news is created and consumed. 
    By leveraging cutting-edge **Generative AI**, we aspire to provide **reliable, real-time, and personalized news content** that empowers individuals and organizations worldwide. 
    We envision a world where technology enhances the accessibility and quality of information for everyone.
    """)

    # Section 2: Our Mission
    st.markdown("---")
    st.markdown("<h2 style='font-size: 30px;'>🚀 Our Mission</h2>", unsafe_allow_html=True)
    st.write("""
    Our mission is simple: to deliver **AI-powered solutions** that make news creation faster, smarter, and more efficient. 
    We believe in innovation, creativity, and the potential of AI to transform industries. Whether you're a journalist, an organization, or just someone seeking personalized content, 
    **AI News Generator** is here to serve your needs with **accuracy, diversity, and creativity**.
    """)

    # Team Section
    st.header("Meet the Team")
    team_members = [
        {
            "name": "Muhammad Khaqan Nasir",
            "github": "KhaqanNasir",
            "linkedin": "khaqan-nasir",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member01.jpg')
        },
        {
            "name": "Muhammad Adnan Tariq",
            "github": "adnaan-tariq",
            "linkedin": "adnaantariq",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member02.JPG')
        },
        {
            "name": "Muhammad Ibtisiam Afzal",
            "github": "ibtisamafzal",
            "linkedin": "ibtisamafzal",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member03.JPG')
        }
    ]

    cols = st.columns(len(team_members))
    for col, member in zip(cols, team_members):
        with col:
            # Encode image to base64
            encoded_image = encode_image(member['image'])
        
            # HTML structure with background color and adjusted image height
            st.markdown(f"""
            <div style='background-color: #f8f9fa; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center;'>
                <div style='background-color: #ffffff; border-radius: 50%; width: 200px; height: 200px; margin: 0 auto; display: flex; justify-content: center; align-items: center;'>
                    <img src="data:image/jpeg;base64,{encoded_image}" alt="{member['name']}" style='width: 100%; height: 100%; object-fit: cover; border-radius: 50%;'>
                </div>
                <div style='font-size: 22px; font-weight: 600; color: #5F6366; margin-top: 10px;'>{member['name']}</div>
                <div style='font-size: 18px; color: #5F6366; margin-top: 5px;'>
                    <a href='https://github.com/{member["github"]}' target='_blank' style='font-size: 20px; color: #000000; margin-right: 10px;'>
                        <i class="fab fa-github" style="font-size: 20px; color: #000000; margin-right: 5px;"></i> GitHub
                    </a>
                    <a href='https://linkedin.com/in/{member["linkedin"]}' target='_blank' style='font-size: 20px; color: #0077B5;'>
                        <i class="fab fa-linkedin" style="font-size: 20px; color: #0077B5; margin-right: 5px;"></i> LinkedIn
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Section 4: Technology Stack
    st.markdown("---")
    st.markdown("<h2 style='font-size: 30px;'>🛠️ Technology Stack</h2>", unsafe_allow_html=True)
    st.write("""
    Our app uses cutting-edge **Generative AI models** combined with open-source tools to ensure high-quality performance. 
    Below are some key technologies that power **AI News Generator**:
    - **Streamlit**: For building the user interface.
    - **Natural Language Processing (NLP)**: For generating accurate and readable news content.
    - **Free APIs and Open-Source Models**: To make the app cost-efficient and widely accessible.
    - **Python Libraries**: For seamless backend integration and feature enhancement.
    """)

    # Section 5: Why Choose Us?
    st.markdown("---")
    st.markdown("<h2 style='font-size: 30px;'>💡 Why Choose Us?</h2>", unsafe_allow_html=True)
    st.write("""
    - **Free and Accessible**: We use free resources to ensure accessibility for all users.
    - **Real-Time News**: Generate fresh, personalized news in seconds.
    - **Innovative AI**: Powered by state-of-the-art generative AI.
    - **User-Centric Design**: Intuitive and simple to use for anyone.
    """)

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
        unsafe_allow_html=True
    )
    st.sidebar.success("Select a page above.")

# Function to encode image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        import base64
        return base64.b64encode(image_file.read()).decode("utf-8")

# Run the app
if __name__ == "__main__":
    main()
