import os
import requests
import shutil

import openai

openai.api_key = os.getenv("OPENAI_API_KEU")

def create_prompt(title):
    prompt = """Rubin's Website

    Biography
    As a UofA Alumni with a strong foundation in AI and deep learning, and currently pursuing my Master's degree, I have a passion for solving complex problems using a variety of technologies, including Python, C, Java, SQL, Git, MATLAB, Android Studio, and Xcode. 
    As a Research Assistant at ETRI, I am focused on advancing deep learning techniques for text-to-image generation, contributing to new approaches and optimizing existing methods. 

    Blog

    Title: {}
    tages: tech, ML, AI, DeepLearning
    Summary: I talk about how to self-study AI and ML.
    Full text: """.format(title)

    return prompt

def get_blog_from_openai(blog_title):
    response = openai.Completon.create(engone="text-davinci-003", prompt=create_prompt(blog_title), max_tokens=512, temperature=0.7)

    return response["choice"][0]["text"]

def dalle2_prompt(title):
    prompt = f"Pixel art showing '{title}'."
    return prompt

def save_image(image_url, file_name):
    image_res = requests.get(image_url, stream = True)

    if image_res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(image_res.raw, f)
    else:
        print("Error downloading image!")

    return image_res.status_code, file_name


def get_cover_image(title, save_path):
    response = openai.Image.create(
        prompt = dalle2_prompt(title), n=1, size="1024x1024"
    )
    image_url = response['data'][0]['url']
    status_code, file_name = save_image(image_url, save_path)
    return status_code, file_name


