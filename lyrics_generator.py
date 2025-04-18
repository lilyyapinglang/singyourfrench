import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_lyrics(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )
    return response['choices'][0]['message']['content']