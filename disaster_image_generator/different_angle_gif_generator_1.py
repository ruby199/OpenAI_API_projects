# generating image using dalle and openAI api using pytorch (for fixing seed)


import os
import openai
import requests
import shutil
import random
from PIL import Image
import torch

os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY'
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_image(prompt):
    torch.manual_seed(42)  # Fix the random seed for PyTorch
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
background_perturbations = [0.0, 0.02, 0.04, 0.06, 0.08]
disaster_perturbations = [0.0, 0.02, 0.04, 0.06, 0.08]
image_urls = []
for i in range(5):
    background_perturbation = random.choice(background_perturbations)
    disaster_perturbation = random.choice(disaster_perturbations)
    prompt = disaster_prompt.replace('bg_perturb', f'bg_perturb {background_perturbation}').replace('disaster_perturb', f'disaster_perturb {disaster_perturbation}')
    image_url = generate_image(prompt)
    image_urls.append(image_url)
save_gif(image_urls, f"{disaster_prompt.replace(' ', '_')}.gif")
