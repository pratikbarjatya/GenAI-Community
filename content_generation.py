from diffusers import StableDiffusionPipeline
from transformers import pipeline
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Hugging Face API Token
HUGGING_FACE_TOKEN = "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"

# Logging Function
def log_error(message):
    """Logs error messages to a file."""
    with open("error_logs.txt", "a") as log_file:
        log_file.write(f"{message}\n")

# 1. Text Post Generation
def generate_text_post(summary, tone, platform):
    """Generates a text post using Hugging Face GPT-2."""
    try:
        generator = pipeline("text-generation", model="gpt2", tokenizer="gpt2", use_auth_token=HUGGING_FACE_TOKEN)
        prompt = f"Generate a {tone} {platform} post: {summary}"
        post = generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]
        return post
    except Exception as e:
        log_error(f"Error generating text post: {e}")
        return "Error generating text post."

# 2. Image Generation using Stable Diffusion
def generate_image(prompt):
    """Generates an image using Stable Diffusion."""
    try:
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5", use_auth_token=HUGGING_FACE_TOKEN
        )
        image = pipe(prompt).images[0]
        image_path = "generated_image.png"
        image.save(image_path)
        return image_path
    except Exception as e:
        log_error(f"Error generating image: {e}")
        return None

# 3. Video Generation
def generate_video(prompt):
    """Generates a video using Hugging Face API."""
    try:
        api_url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
        headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}
        payload = {"inputs": prompt}
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        video_url = response.json().get("generated_video_url")
        if not video_url:
            raise Exception("API did not return a video URL.")
        video_response = requests.get(video_url)
        video_path = "generated_video.mp4"
        with open(video_path, "wb") as f:
            f.write(video_response.content)
        return video_path
    except Exception as e:
        log_error(f"Error generating video: {e}")
        return None

# 4. Meme Generation
def generate_meme(caption):
    """Generates a meme by overlaying text on a template."""
    try:
        meme_url = "https://i.imgflip.com/1bij.jpg"  # Example: Drake meme
        response = requests.get(meme_url)
        image = Image.open(BytesIO(response.content))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text((20, 20), caption, font=font, fill="white")
        meme_path = "generated_meme.jpg"
        image.save(meme_path)
        return meme_path
    except Exception as e:
        log_error(f"Error generating meme: {e}")
        return None
