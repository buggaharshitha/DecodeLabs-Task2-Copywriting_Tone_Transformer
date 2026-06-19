from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("=" * 50)
print(" Automated Copywriting & Tone Transformer ")
print("=" * 50)

# User inputs
product_name = input("Enter Product Name: ")
platform = input("Enter Platform (Instagram/LinkedIn/Email): ")
tone = input("Enter Tone (Professional/Friendly/Formal): ")

# Prompt
prompt = f"""
You are an expert marketing copywriter.

Create a {tone} marketing post for the following product.

Product Name: {product_name}
Platform: {platform}

Requirements:
- Make it engaging.
- Match the selected tone.
- Optimize it for the selected platform.
- Include a strong call-to-action.
"""

# Generate content
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print("\nGenerated Marketing Copy:\n")
print(response.text)