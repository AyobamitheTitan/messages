from typing import Optional
from pydantic import BaseModel
from enums import EmailType

class MailtrapEmailSchema(BaseModel):
    recipient_email: str
    name: str
    subject: str
    htmlContent: str

class ParseBrevoEmail(BaseModel):
    email: str
    recipient_name:str
    email_type: EmailType
    code: Optional[str] = None