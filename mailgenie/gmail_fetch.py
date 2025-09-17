import os
import datetime
import base64
import sys

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# ---------------------------------------------------------------------
# Demo emails for recruiters (mock mode)
# ---------------------------------------------------------------------
def load_mock_emails():
    return [
        {
            "subject": "Approve Project Proposal",
            "snippet": "Please review and approve the attached proposal.",
            "from": "manager@example.com",
        },
        {
            "subject": "Team Lunch Invitation",
            "snippet": "Join us for lunch at 1 PM tomorrow.",
            "from": "teammate@example.com",
        },
        {
            "subject": "Urgent: Server Down",
            "snippet": "The production server is currently down, need help ASAP!",
            "from": "it-support@example.com",
        },
    ]


# ---------------------------------------------------------------------
# Real Gmail fetch (only used if GMAIL_MODE=real)
# ---------------------------------------------------------------------
def fetch_recent_emails(service, days=2, max_results=50):
    date_after = (datetime.datetime.utcnow() - datetime.timedelta(days=days)).strftime("%Y/%m/%d")
    results = (
        service.users()
        .messages()
        .list(userId="me", q=f"after:{date_after}", maxResults=max_results)
        .execute()
    )
    messages = results.get("messages", [])
    emails = []

    for msg in messages:
        msg_data = service.users().messages().get(userId="me", id=msg["id"]).execute()
        payload = msg_data.get("payload", {})
        headers = payload.get("headers", [])

        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "(No Subject)")
        sender = next((h["value"] for h in headers if h["name"] == "From"), "(Unknown Sender)")
        snippet = msg_data.get("snippet", "")

        emails.append({"subject": subject, "snippet": snippet, "from": sender})

    return emails


# ---------------------------------------------------------------------
# Build the digest text
# ---------------------------------------------------------------------
def build_digest(emails):
    lines = ["\n📬 **MailGenie Digest** 📬", "---------------------------"]
    for i, email in enumerate(emails, start=1):
        lines.append(f"\n{i}. ✉️ Subject: {email['subject']}")
        lines.append(f"   From: {email['from']}")
        lines.append(f"   Snippet: {email['snippet']}")
    return "\n".join(lines)


# ---------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------
if __name__ == "__main__":
    gmail_mode = os.getenv("GMAIL_MODE", "mock").lower()

    if gmail_mode == "mock":
        print("✅ Demo Mode enabled (mock emails).")
        emails = load_mock_emails()
    else:
        print("📡 Real Gmail Mode enabled.")
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json")
        service = build("gmail", "v1", credentials=creds)
        emails = fetch_recent_emails(service)

    if not emails:
        print("⚠️ No emails found.")
        sys.exit(0)

    print(f"\n✅ {len(emails)} emails loaded. Building digest...")
    digest = build_digest(emails)

    print(digest)
    print("\n💌 Demo Mode: Digest built successfully!")
