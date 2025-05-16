import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_summary(entry):
    prompt = f"""
You are a cybersecurity analyst.

Log Info:
- Event: {entry["event_type"]}
- Source IP: {entry["source_ip"]}
- Destination IP: {entry["destination_ip"]}
- Mapped MITRE Technique: {entry["technique"]}

Generate a readable summary for a CISO and SOC team. Include potential impact, threat context, and mitigation advice.
"""
    response = client.chat.completions.create(
         model="llama3-70b-8192",  # You can use llama3-70b-8192 as well
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
