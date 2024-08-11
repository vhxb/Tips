import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    Text = input("Text:\n")
    Prompt = input("Prompt:\n")
    content = Text + Prompt
    messages = [{"role": "user", "content": content}]
    
    response=openai.chat.completions.create(
          model="gpt-3.5-turbo-0125",
          messages=messages
        )

    answer = response.choices[0].message.content
    print(f'ChatGPT: {answer}\n\n\n')
