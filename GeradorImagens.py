import os
from openai import OpenAI
from dotenv import load_dotenv


class GeradorImagens:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('API_KEY')
        self.client = OpenAI(api_key=api_key)

    def gerar(self, prompt):
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1792x1024"
        )
        print(response)
        return response
