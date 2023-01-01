import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.organization = os.getenv("openai_organization")
openai.api_key = os.getenv("openai_api_key")
# openai.Model.list()


def generate_image(prompt, size, number):
    response = openai.Image.create(
        prompt=prompt,
        n=int(number),
        size=size,
    )

    urls = [image['url'] for image in response['data']]
    image_url = response["data"][0]["url"]
    print(urls)
    return urls

if __name__ == "__main__":
    openai.Model.list()
    response = openai.Image.create(
        prompt="a koala bear playing the tambarine",
        n=2,
        size="256x256",
    )
    urls = [image['url'] for image in response['data']]
    image_url = response["data"][0]["url"]
    print(urls)
    # print(response['data'])
    # image_url = response["data"][0]["url"]
    # print(image_url)
