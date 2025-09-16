# MailGenie — AI-powered smart mail assistant

MailGenie fetches your Gmail securely, categorizes and summarizes emails using a local/hosted Small Language Model (SLM, e.g. Ollama phi3), and surfaces action-required messages first. It was designed as a hackathon demo and extended for recruiters and engineers to evaluate the architecture and UX.

## 🎥 Demo (for recruiters)
- Demo video: `assets/demo.mp4`
- Screenshots: `assets/screenshot-1.png`, `assets/screenshot-2.png`

Recruiters: you don’t need Gmail credentials to see MailGenie in action.  
You can run it in **Demo Mode** with sample emails and mock AI outputs.

```bash
git clone https://github.com/sshambhavi9/mailgenie.git
cd mailgenie
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
pip install -r requirements.txt

# enable demo mode in .env
echo "LLM_MODE=mock" > .env
echo "GMAIL_MODE=mock" >> .env

python mailgenie_app.py
This launches MailGenie with pre-recorded email data so you can see the categorization and summarization pipeline without setting up Google credentials.

✨ Features
Secure Gmail access via OAuth2 (developer mode)

Local/hosted SLM integration (Ollama or compatible) for categorization & summarization

Prioritizes action-required emails

CLI + simple web UI demo

Configurable rules & keyword lists for categories

Demo mode with sample data (no Gmail required)

🛠 Developer Setup (with Gmail API)
If you want to connect MailGenie to your own Gmail, follow these steps.

Prerequisites
Python 3.10+

A Google Cloud project with Gmail API enabled

OAuth credentials (Client ID + Secret)

Ollama or compatible SLM server

1) Clone
bash
Copy code
git clone https://github.com/<your-username>/mailgenie.git
cd mailgenie

2) Configure environment
Copy .env.example into .env:

bash
Copy code
cp .env.example .env
Fill in your details:

ini
Copy code
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret
GOOGLE_REDIRECT_URI=http://localhost:8080/oauth2callback
GOOGLE_REFRESH_TOKEN=your-refresh-token
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=phi3
LLM_MODE=online
GMAIL_MODE=oauth

3) Install dependencies
bash
Copy code
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

4) Enable Gmail API
Open Google Cloud Console

Create/select a project

Enable Gmail API

Create OAuth Client ID (Desktop app is simplest)

Copy Client ID + Secret into .env

5) Get a refresh token
bash
Copy code
python scripts/get_refresh_token.py
Follow the link, grant access, paste the code back. Save the refresh token into .env.

6) Run
bash
Copy code
python mailgenie_app.py
📂 Project Structure
bash
Copy code
mailgenie/
  ├── core/                # Main app logic
  ├── scripts/             # OAuth + helper scripts
  ├── assets/              # Demo video + screenshots
  ├── requirements.txt
  ├── .env.example
  ├── README.md
🔒 Security
.env is ignored in .gitignore

No secrets or credentials committed

Uses OAuth refresh tokens, never raw passwords

Supports GitHub Secrets for CI/CD

🤝 Contributing
Pull requests welcome! For significant changes, please open an issue first to discuss.

📜 License
MIT License
