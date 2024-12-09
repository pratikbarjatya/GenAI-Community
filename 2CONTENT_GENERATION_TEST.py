from content_generation import generate_text_post, generate_image, generate_video, generate_meme

def test_content_generation():
    # Test 1: Text Post Generation
    print("\nTesting Text Post Generation...")
    summary = "AI is replacing repetitive jobs in the tech industry."
    tone = "humorous"
    platform = "Twitter"
    text_post = generate_text_post(summary, tone, platform)
    if text_post:
        print("Text Post Generated:")
        print(text_post)
    else:
        print("Text post generation failed.")

    # Test 2: Image Generation
    print("\nTesting Image Generation...")
    image_prompt = "A futuristic AI robot working in an office."
    image_path = generate_image(image_prompt)
    if image_path:
        print(f"Image Generated and saved at: {image_path}")
    else:
        print("Image generation failed.")

    # Test 3: Video Generation
    print("\nTesting Video Generation...")
    video_prompt = "A robotic arm assembling cars in a factory."
    video_path = generate_video(video_prompt)
    if video_path:
        print(f"Video Generated and saved at: {video_path}")
    else:
        print("Video generation failed.")

    # Test 4: Meme Generation
    print("\nTesting Meme Generation...")
    meme_caption = "AI replacing jobs since 2023!"
    meme_path = generate_meme(meme_caption)
    if meme_path:
        print(f"Meme Generated and saved at: {meme_path}")
    else:
        print("Meme generation failed.")

if __name__ == "__main__":
    test_content_generation()
