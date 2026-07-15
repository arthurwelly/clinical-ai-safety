# Clinical AI Safety: Auditing LLM Alignment in Psychological Distress Scenarios

As conversational AIs are increasingly used by the general public as confidants, evaluating their behavioral and safety boundaries is critical. This repository documents red teaming audits of commercial LLMs interacting with simulated users experiencing acute psychological distress (such as PTSD). By analyzing issues like clinical sycophancy, this project aims to propose concrete, clinical-backed mitigation strategies to build safer conversational systems.

## 👤 About Me

I have a **tech background in Computer Science** and I am a **practicing Clinical Psychologist** specializing in trauma support. 
This dual perspective allows me to look at AI safety through a human lens. Instead of searching for standard code exploits, I audit AI models for "cognitive bugs" where a model's enthusiasm to please might accidentally validate unhealthy behaviors or harm a vulnerable user during a sensitive mental health conversation.

---

## 📂 Active Safety Audits

| Case Study | Tested Models | Key Finding | Status |
| :--- | :--- | :--- | :---: |
| [01: AI Sycophancy & PTSD Avoidance](./01-clinical-sycophancy) | Mistral, ChatGPT, Claude, Gemini | 1 critical failure (iatrogenic validation) | Completed |

---

## 🛠️ Methodology

* **Testing Beyond English:** I run my audits in French (with English translations). AI safety filters are often weaker in languages other than English.
* **Real-World Scenarios:** I don't use abstract tests. I design realistic prompts based on my daily clinical experience, to see how an AI truly handles real human struggles.
* **Building Solutions:** The goal is to highlight these hidden gaps and offer practical fixes to help developers build safer conversational tools.
