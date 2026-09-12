import os

from dotenv import load_dotenv
from openai import OpenAI


# Load variables from .env
load_dotenv()

# Create the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Send a request to the model
response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful research assistant.",
    input="Explain quantum computing in 3 simple bullet points."
)

# Print the answer
print(response.output_text)