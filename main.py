import os
from google import genai
import base64


client = genai.Client(api_key = 'Your_api_key')

def on_message():
    prompt_= input("Enter the Prompt to generate the image: ")
    result = client.models.generate_content(model = "gemini-2.5-flash-image"
                                    ,contents = prompt_
                                    )

    image_base64 = result.data[0].b64_json

    with open("Generated_image.png", "wb") as f:
        f.write(image.image_bytes)


    print("Image saved as genertaed_image.png")


on_message()
