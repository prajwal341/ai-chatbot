import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Fallback FAQ (backup if AI fails)
faq = {
    "hello": "Hello! How can I assist you today?",
    "fees": "Course fees depend on the program.",
    "duration": "Course duration is 3 months.",
    "course": "We offer AI, Web Development, and Python courses.",
    "certificate": "Yes, we provide certificates.",
    "placement": "We offer placement support.",
    "bye": "Goodbye! Have a great day!"
}

def get_response(user_input):
    try:
        # AI response
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional customer support assistant. Answer clearly and politely."},
                {"role": "user", "content": user_input}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("AI Error:", e)

        # fallback if AI fails
        user_input = user_input.lower()
        for key in faq:
            if key in user_input:
                return faq[key]

        return "Sorry, I'm facing a technical issue right now."   
