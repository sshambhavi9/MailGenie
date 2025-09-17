from fastapi import FastAPI

app = FastAPI(title="MailGenie: SmartMail Assistant")

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

# Optional: Demo digest endpoint for recruiters
@app.get("/api/demo-digest")
def demo_digest():
    return {
        "Action Required": [
            {"time": "09:00", "sender": "Alice", "subject": "Approve Project Proposal"},
        ],
        "Personal": [
            {"time": "12:30", "sender": "Bob", "subject": "Team Lunch Invitation"},
        ],
        "Urgent": [
            {"time": "14:15", "sender": "IT Alerts", "subject": "Server Down - Immediate Action Required"},
        ]
    }
