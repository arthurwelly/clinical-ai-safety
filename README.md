# Clinical AI Safety: Auditing LLM Alignment in Psychological Distress Scenarios

As conversational AIs are increasingly used by the general public as confidants, evaluating their behavioral and safety boundaries is critical. This repository documents red teaming audits of commercial LLMs interacting with simulated users experiencing acute psychological distress (such as PTSD). By analyzing failure modes like clinical sycophancy and deference to medical authority, this project aims to propose concrete, clinically-backed mitigation strategies to build safer conversational systems.

## 👤 About Me

I have a **tech background in Computer Science** and I am a **practicing Clinical Psychologist** specializing in trauma support.
This dual perspective allows me to look at AI safety through a human lens. Instead of searching for standard code exploits, I audit AI models for "cognitive bugs" — cases where a model's enthusiasm to please validates unhealthy behaviors, or where it withholds clinical information precisely when a vulnerable user would need it most.

---

## 📂 Active Safety Audits

| Case Study | Tested Models | Key Finding | Status |
| :--- | :--- | :--- | :---: |
| [01: AI Sycophancy & PTSD Avoidance](./01-clinical-sycophancy) | Mistral, ChatGPT, Claude, Gemini | 1 critical failure (iatrogenic validation) | Completed |
| [02: Medical Authority & Contraindicated Prescription](./02-authority-contraindication) | GPT-5.5, Mistral Medium, Claude Sonnet 5, Gemini Flash | All 4 models state the contraindication when asked directly (12/12); none do once a prescriber is mentioned (0/12) | Completed |

---

## 🛠️ Methodology

* **Clinically grounded scenarios:** I don't use abstract tests. Scenarios are built from established clinical guidelines and realistic patient presentations drawn from daily practice.
* **Controlled comparison:** Where possible, conditions differ by a single clause, so an observed effect can be attributed to a specific variable.
* **Multilingual testing:** Audits are run in French and English. Safety behaviors may differ across languages.
* **Reproducible tooling:** From case 02 onward, audits use [Promptfoo](https://github.com/promptfoo/promptfoo) with published configuration files and raw results, so anyone can re-run them.
* **Building solutions:** The goal is to highlight these hidden gaps and offer practical fixes to help developers build safer conversational tools.
