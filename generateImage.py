import os

import openai


def generate_image(user_prompt, num_images=1, image_size="1024x1024"):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Image.create(
        prompt=user_prompt,
        n=num_images,
        size=image_size
    )

    image_urls = [data['url'] for data in response.get('data', [])]
    return image_urls
