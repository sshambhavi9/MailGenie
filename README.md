# MailGenie — AI-powered Smart Mail Assistant

**MailGenie** fetches your Gmail securely, categorizes and summarizes emails using a local/hosted Small Language Model (SLM, e.g. Ollama phi3), and surfaces action-required messages first.  

This repo includes a **Demo Mode** for recruiters to try the project **without Gmail credentials**.

---

## 🎥 Demo (Recruiters)

**Key point:** You **do not need Gmail credentials** to see MailGenie in action. Demo Mode loads sample emails and opens the digest automatically in your browser.

---

## ✨ Features

- Secure Gmail access via OAuth2 (developer mode)
- Local/hosted SLM integration (Ollama or compatible) for categorization & summarization
- Prioritizes action-required emails
- CLI + browser output demo
- Configurable rules & keyword lists for categories
- Demo mode with sample data (no Gmail required)

---

## 🏃 Running Demo Mode (Recruiters)

1. Clone the repository:
git clone https://github.com/<your-username>/MailGenie.git
cd MailGenie

2. Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Enable Demo Mode:
echo "LLM_MODE=mock" > .env
echo "GMAIL_MODE=mock" >> .env
export $(cat .env | xargs)

6. Run MailGenie:
python3 gmail_fetch.py
The digest will open automatically in your browser, showing sample categorized emails and summaries.

## 🛠 Developer Setup (with Gmail API)

Prerequisites
- Python 3.10+

- A Google Cloud project with Gmail API enabled

- OAuth credentials (Client ID + Secret)

- Ollama or compatible SLM server

Steps
1. Clone the repository (if not already done):
git clone https://github.com/<your-username>/MailGenie.git
cd MailGenie

2. Copy .env.example to .env:
cp .env.example .env

3. Fill in your credentials and settings in .env:
- GOOGLE_CLIENT_ID=your-client-id
- GOOGLE_CLIENT_SECRET=your-client-secret
- GOOGLE_REDIRECT_URI=http://localhost:8080/oauth2callback
- GOOGLE_REFRESH_TOKEN=your-refresh-token
- OLLAMA_HOST=http://localhost:11434
- OLLAMA_MODEL=phi3
- LLM_MODE=onlineGMAIL_MODE=oauth

4. Install dependencies:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

5. Enable Gmail API in Google Cloud Console and get a refresh token:
python3 scripts/get_refresh_token.py

6. Run MailGenie:
python3 gmail_fetch.py


## 🔒 Security
.env is ignored in .gitignore

No secrets or credentials are committed

Uses OAuth refresh tokens, never raw passwords

Supports GitHub Secrets for CI/CD

## 🤝 Contributing
Pull requests welcome! For significant changes, please open an issue first to discuss.

## 📜 License
MIT License
