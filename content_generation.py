import openai
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from transformers import pipeline, StableDiffusionPipeline
import os

# Set your Hugging Face token
HUGGING_FACE_TOKEN = "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"

# Function to log errors to a file
def log_error(message):
    """Logs error messages to a file."""
    with open("error_logs.txt", "a") as log_file:
        log_file.write(f"{message}\n")

# Text Generation using Hugging Face GPT (GPT-2 or GPT-3)
def generate_text_post(summary, tone, platform):
    try:
        # Load text generation model (GPT-2 or GPT-3 via Hugging Face)
        generator = pipeline("text-generation", model="gpt2", tokenizer="gpt2", use_auth_token=HUGGING_FACE_TOKEN)
        
        # Format the post with tone and platform
        prompt = f"Generate a {tone} {platform} post: {summary}"

        # Generate the text post
        post = generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]
        return post
    except Exception as e:
        error_message = f"Error generating text post: {e}"
        log_error(error_message)
        return error_message

# Image Generation using Stable Diffusion or DALL·E (Hugging Face)
def generate_image(prompt):
    try:
        # Load Stable Diffusion model for image generation
        pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v-1-4-original", use_auth_token=HUGGING_FACE_TOKEN)
        
        # Generate the image
        image = pipe(prompt).images[0]
        image.save("generated_image.png")
        return "generated_image.png"
    except Exception as e:
        error_message = f"Error generating image: {e}"
        log_error(error_message)
        return error_message

# Meme Generation by adding text to a template using PIL
def generate_meme(caption):
    try:
        # Example meme template (using the 'Distracted Boyfriend' meme template)
        meme_url = "https://i.imgflip.com/1bij.jpg"  # Replace with actual URL
        response = requests.get(meme_url)
        image = Image.open(BytesIO(response.content))

        # Add caption to the meme
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text((20, 20), caption, font=font, fill="white")
        
        meme_path = "generated_meme.jpg"
        image.save(meme_path)
        return meme_path
    except Exception as e:
        error_message = f"Error generating meme: {e}"
        log_error(error_message)
        return error_message
