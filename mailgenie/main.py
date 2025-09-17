from fastapi import FastAPI

app = FastAPI(title="MailGenie: SmartMail Assistant")


@app.get("/api/health")
def health_check():
    return {"status": "ok"}
