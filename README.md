# GenAI Community Project

This repository contains the code for the GenAI Community project, which was part of a hackathon hosted by [GenAI Works](https://genai.works/hackathon).

## Overview

The GenAI Community project aims to leverage AI technologies to generate various types of content, including text posts, images, videos, and memes. The project utilizes APIs from Hugging Face and Groq to perform tasks such as sentiment analysis, text generation, image generation, and news retrieval.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/adnaan-tariq/GenAI-Community.git
   cd GenAI-Community
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory of the project.
   - Add your API keys for Hugging Face and Groq in the `.env` file:
     ```
     HUGGING_FACE_API=your_hugging_face_api_key
     GROQ_API_KEY=your_groq_api_key
     NEWS_API_KEY=your_news_api_key
     ```

## Usage

To run the project, use the following command:
```bash
streamlit run main_app.py
```

This will start a Streamlit web application where you can input prompts and generate content based on the selected options.

## Features

- **Text Post Generation**: Generate text posts using Hugging Face GPT-2.
- **Image Generation**: Generate images using Stable Diffusion.
- **Video Generation**: Generate videos using Hugging Face API.
- **Meme Generation**: Generate memes by overlaying text on a template.
- **News Retrieval**: Fetch news articles based on user prompts and summarize them.

## Hackathon

This project was part of a hackathon hosted by [GenAI Works](https://genai.works/hackathon). The goal was to create an AI-driven content generation tool that can assist users in creating engaging content for various platforms.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
