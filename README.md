# 🕵️‍♂️ Context-Aware Security Threat Narrator

A Generative AI tool that transforms raw cybersecurity logs into executive-ready incident summaries using MITRE ATT&CK mapping and Groq-powered LLMs.

🚀 Built as part of my [30-Day Generative AI Challenge](#), this project is tailored for **CISOs**, **SOC teams**, and **Legal/Compliance departments** to receive readable, actionable intelligence derived from technical logs.

---

## 📌 What It Does

Given structured threat logs (e.g., from SIEM tools like Elastic or Splunk), the app:

- 🔎 Parses event metadata (IP addresses, tool used, event type)
- 🧠 Maps events to MITRE ATT&CK techniques
- 🤖 Generates contextual summaries using **Groq’s LLaMA3-70B**
- 📄 Delivers readable incident reports with **impact, threat intent, and mitigation advice**

---

## 🛠️ Tech Stack

| Component     | Technology                             |
|---------------|----------------------------------------|
| LLM Backend   | [Groq API](https://console.groq.com/)  |
| Threat Intel  | [MITRE ATT&CK](https://attack.mitre.org/) |
| Language      | Python 3.9+                            |
| Frontend      | [Gradio](https://www.gradio.app/) UI   |
| Deployment    | Local or Cloud (Streamlit/Spaces)      |

---

## 🧪 Sample Input (CSV)

```csv
timestamp,source_ip,destination_ip,event_type,tool_used
2025-05-16 12:01:23,192.168.1.101,10.0.0.20,powershell,powershell.exe
2025-05-16 12:03:44,192.168.1.102,8.8.8.8,dns exfil,nslookup
```

✅ Example Output
Event: PowerShell Execution
Mapped MITRE: Execution > PowerShell
Summary:
A PowerShell execution from internal host 192.168.1.101 targeting 10.0.0.20 indicates possible lateral movement or remote code execution. This aligns with MITRE technique T1059.001. Immediate investigation is recommended...

🧩 Folder Structure
```bash
threat-narrator/
├── main.py
├── log_parser.py
├── mitre_mapper.py
├── summary_generator.py
├── sample_logs.csv
├── requirements.txt
├── .env
└── README.md
```

📦 Installation
1. Clone the repo:
```bash
git clone https://github.com/your-username/threat-narrator.git
cd threat-narrator
```

2. Create & activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file:
```env
GROQ_API_KEY=your_groq_api_key_here
```
5. Run the app:
```bash
python main.py
```

🧠 What I Learned
Mapping real-world logs to MITRE ATT&CK improves threat narrative clarity
How to use Groq to run LLMs like llama3-70b at high speed
Prompt engineering to generate audience-specific summaries
Building an AI system that's actually usable for security professionals

🚧 Future Improvements
Add role-based output mode (CISO, SOC, Legal)
Incorporate threat severity scoring
Export summaries to PDF or Markdown reports
Implement RAG using a custom knowledge base of past incidents

📬 Connect with Me
I'm building one GenAI project every day for 30 days.
Follow my journey on LinkedIn or ⭐️ this repo if you found it helpful!
