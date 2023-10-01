import openai
import random
import os
import midiutil

def get_mood(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"{prompt}\nMood:",
        temperature=0.7,
        max_tokens=10
    )
    mood = response['choices'][0]['text'].strip()
    return mood

def generate_music(mood):
    # ... (rest of your function)

if __name__ == "__main__":
    # Set the API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # User's prompt
    user_prompt = "Describe a joyful celebration."
    # Get mood from GPT-3
    mood = get_mood(user_prompt)
    # Generate music based on mood
    generate_music(mood)
