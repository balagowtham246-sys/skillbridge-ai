import openai, os
openai.api_key = os.getenv("OPENAI_API_KEY")

def detect_domain(query):
    prompt = f"Given this skill or interest '{query}', which tech domain (like AI, Web Dev, Cybersecurity, etc.) does it belong to?"
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are an expert career guide."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
