import nltk
nltk.download('punkt')

# download only if not already
try:
    nltk.data.find('tokenizers/punkt')
except:
    nltk.download('punkt')

faq = {
    "hello": "Hi! How can I assist you today?",
    "hi": "Hello! What can I help you with?",
    "fees": "Course fees depend on the program.",
    "duration": "Course duration is 3 months.",
    "course": "We offer AI, Web Development, and Python courses.",
    "certificate": "Yes, we provide certificates.",
    "placement": "We offer placement support.",
    "bye": "Goodbye! Have a great day!"
}

def get_response(user_input):
    user_input = user_input.lower()

    for key in faq:
        if key in user_input:
            return faq[key]

    return "Sorry, I didn't understand that."   
