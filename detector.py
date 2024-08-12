import asyncio
import base64
import os
import time
import aiohttp
import cv2

import pygame

pygame.mixer.init()
os.environ["OPENAI_API_KEY"] = "api_key"

def encode_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Compress the image
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 20]
    _, buffer = cv2.imencode('.jpg', image, encode_param)

    # Convert to base64
    base64_image = base64.b64encode(buffer).decode('utf-8')
    return base64_image


async def detect_hand_near_mouth(image_path):
    """Uses OpenAI's GPT model to describe the image and check for 'hand near mouth'."""
    base64_image = encode_image(image_path)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {os.environ["OPENAI_API_KEY"]}'
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "does the person has his fingers in his mouth? answer only with yes or no"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload) as response:
            result = await response.json()

    description = result['choices'][0]['message']['content'].lower()
    return 'yes' in description


async def main():
    cap = cv2.VideoCapture(0)
    sound_playing = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        image_path = 'current_frame.jpg'
        cv2.imwrite(image_path, frame)

        if await detect_hand_near_mouth(image_path):
            if not sound_playing:
                pygame.mixer.music.load('alert_sound.mp3')
                pygame.mixer.music.play(-1)  # Play in a loop
                sound_playing = True
        else:
            if sound_playing:
                pygame.mixer.music.stop()
                sound_playing = False


        time.sleep(0.5)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    asyncio.run(main())
