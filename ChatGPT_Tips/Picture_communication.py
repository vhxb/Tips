from openai import OpenAI
client = OpenAI()



# Prompt. 
Prompt="""
What are in these images in urls?"""

messages = [
    {
        "role": "user", 
        "content": [
            {"type": "text", 
             "text": Prompt,
            },
            {
              "type": "image_url",
              "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                            "detail": "high",}
            },

          ],
    }
]



# Processing by openai.
# Chat Completions response format:https://platform.openai.com/docs/guides/chat-completions/response-format
response=client.chat.completions.create(
  model="gpt-4o-mini-2024-07-18",
  messages=messages,
)
result = response.choices[0].message.content



import os
from datetime import datetime

current_time = datetime.now().strftime("%y%m%d_%H%M_%S")
file_name = f"{current_time}.txt"

file_path = os.path.join(r'C:\Users\vhxb\Documents\GPT_API_Response', file_name)
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(result)
os.startfile(file_path)
