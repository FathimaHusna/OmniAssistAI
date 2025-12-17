from langchain_core.tools import tool
import random
import datetime

@tool
def create_ticket(title: str, description: str, priority: str = "Medium") -> str:
    """
    Creates a support ticket in the ticketing system.
    Use this when the user reports an issue or requests a new feature that needs tracking.
    """
    ticket_id = f"TICKET-{random.randint(1000, 9999)}"
    print(f"[MOCK ACTION] Creating Ticket: {ticket_id} | Title: {title} | Priority: {priority}")
    return f"Ticket {ticket_id} created successfully. Title: {title}, Priority: {priority}."

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import settings

@tool
def send_email(recipient: str, subject: str, body: str) -> str:
    """
    Sends an email to the specified recipient using SMTP.
    Use this when the user explicitly asks to send an email or notify someone.
    ALWAYS ask for confirmation before calling this tool unless the user has already confirmed.
    """
    if not settings.SMTP_USERNAME or not settings.SMTP_PASSWORD:
        return "Error: SMTP credentials are not configured in the server."

    try:
        msg = MIMEMultipart()
        msg['From'] = settings.SMTP_USERNAME
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT)
        server.starttls()
        server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(settings.SMTP_USERNAME, recipient, text)
        server.quit()
        
        print(f"[ACTION] Sent Real Email to {recipient} | Subject: {subject}")
        return f"Email sent successfully to {recipient}."
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
        return f"Failed to send email: {e}"

@tool
def schedule_meeting(topic: str, time: str, attendees: str) -> str:
    """
    Schedules a meeting on the calendar.
    Use this when the user wants to set up a meeting or appointment.
    Time should be a string describing the time (e.g., 'tomorrow at 2pm').
    """
    print(f"[MOCK ACTION] Scheduling Meeting: {topic} at {time} with {attendees}")
    return f"Meeting '{topic}' scheduled for {time} with {attendees}."
