from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr

app = FastAPI()

app.mount("/static", StaticFiles(directory="mycv_fastapi/static"), name="static")
templates = Jinja2Templates(directory="mycv_fastapi/templates")

conf = ConnectionConfig(
    MAIL_USERNAME="2022uee0152@iitjammu.ac.in",
    MAIL_PASSWORD="vghn oliz rmxr tapp",
    MAIL_FROM="2022uee0152@iitjammu.ac.in",
    MAIL_PORT=587,
    MAIL_FROM_NAME="Your Website",
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/send-email")
async def send_email(request: Request):
    form_data = await request.form()
    name = form_data.get("name")
    email = form_data.get("email")
    subject = form_data.get("subject")
    message = form_data.get("message")

    email_body = f"""
    Name: {name}
    Email: {email}

    Message:
    {message}
    """

    message = MessageSchema(
        subject=f"New Contact Form: {subject}",
        recipients=["2022uee0152@iitjammu.ac.in"],
        body=email_body,
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)

    return {"message": "Email sent successfully!"}
