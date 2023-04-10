# generating image using dalle and openAI api

import os
import openai
import requests
import shutil
import random
from PIL import Image

os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY'
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size='512x512',
        response_format='url',
        model='image-alpha-001'
    )
    image_url = response['data'][0]['url']
    return image_url

def save_gif(image_urls, file_name):
    images = []
    for image_url in image_urls:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            image = Image.open(response.raw)
            images.append(image)
        else:
            print('ERROR LOADING IMAGE')
    images[0].save(
        file_name,
        save_all=True,
        append_images=images[1:],
        optimize=False,
        duration=1000 / 10,  # 10 fps
        loop=0
    )

disaster_prompt = input("Enter the disaster prompt: ")
angles = [0, 45, 90, 135, 180]
image_urls = []
for angle in angles:
    prompt = disaster_prompt.replace('{angle}', str(angle))
    image_url = generate_image(prompt)
    image_urls.append(image_url)
save_gif(image_urls, f"{disaster_prompt.replace(' ', '_')}.gif")
