from json import dumps
from requests import post
from typing import Dict

from enums import EmailType
from templates import ONBOARDING, CODE, EXPIRED_EXCHANGE,PASSWORD_RESET, PROFILE_CHANGE, PAID_EXCHANGE
from schemas import MailtrapEmailSchema
from config.email_provider import EMAIL_PROVIDERS, TEXT_PROVIDER
from typing import Any
from .ebulksms import EbulkSMS

provider: Dict[str,Any] = EMAIL_PROVIDERS.get('provider3')
text_provider: Dict[str,Any] = TEXT_PROVIDER.get('provider1')

class MessageService:
    @staticmethod
    def sendBrevo(
        mailtrap_request: dict,
        error_raiser
    ):
        try:
            mail = None
            match mailtrap_request.get('email_type'):
                case EmailType.ONBOARDING:
                    mail = MailtrapEmailSchema(
                        recipient_email=mailtrap_request.get('email'),
                        name=mailtrap_request.get('recipient_name'),
                        subject="User Onboarding",
                        htmlContent=ONBOARDING\
                            .substitute(
                                {"name":mailtrap_request.get('recipient_name')\
                                ,"code":mailtrap_request.get('code')})
                    )
                case EmailType.PASSWORD_RESET:
                    mail = MailtrapEmailSchema(
                        recipient_email=mailtrap_request['email'],
                        name=mailtrap_request['recipient_name'],
                        subject="Password Reset",
                        htmlContent=PASSWORD_RESET\
                            .substitute({"name":mailtrap_request['recipient_name']})
                    )
                case EmailType.CODE:
                    mail = MailtrapEmailSchema(
                        recipient_email=mailtrap_request['email'],
                        name=mailtrap_request['recipient_name'],
                        subject="Requested Code",
                        htmlContent=CODE\
                            .substitute(
                                {"name":mailtrap_request['recipient_name']\
                                ,"action":mailtrap_request.get("action") or "action","code":mailtrap_request['code']})
                    )
                case EmailType.PASSWORD_RESET_CODE:
                    mail = MailtrapEmailSchema(
                        recipient_email=mailtrap_request['email'],
                        name=mailtrap_request['recipient_name'],
                        subject="Requested Code",
                        htmlContent=CODE\
                            .substitute(
                                {"name":mailtrap_request['recipient_name'],
                                "action":mailtrap_request.get('action','action'),"code":mailtrap_request['code']})
                    )
                case EmailType.EXPIRED_EXCHANGE:
                    mail = MailtrapEmailSchema(
                        recipient_email=mailtrap_request['email'],
                        name=mailtrap_request['recipient_name'],
                        subject="Expired Swap",
                        htmlContent=EXPIRED_EXCHANGE\
                            .substitute({
                                "name":mailtrap_request["recipient_name"],
                                "exchange":mailtrap_request["exchange_type"],
                                "reference":mailtrap_request["reference"]
                            })
                    )
                case EmailType.COMPLETED_EXCHANGE:
                    mail = MailtrapEmailSchema(
                        recipient_email=mailtrap_request['email'],
                        name=mailtrap_request['recipient_name'],
                        subject=f"Completed {mailtrap_request.get('exchange_type')}",
                        htmlContent=EXPIRED_EXCHANGE\
                            .substitute({
                                "name":mailtrap_request["recipient_name"],
                                "exchange":mailtrap_request["exchange_type"],
                                "reference":mailtrap_request["reference"]
                            })
                    )
                case EmailType.PROFILE_CHANGE:
                    mail = MailtrapEmailSchema(
                        recipient_email=mailtrap_request["email"],
                        name=mailtrap_request["recipient_name"],
                        subject=f"Profile change",
                        htmlContent=PROFILE_CHANGE\
                            .substitute({
                                "name":mailtrap_request["recipient_name"],
                                "profile_entity":mailtrap_request["profile_entity"]
                            })
                    )
                case EmailType.PAID_EXCHANGE:
                    mail = MailtrapEmailSchema(
                        recipient_email=mailtrap_request["email"],
                        name=mailtrap_request["recipient_name"],
                        subject=f"{mailtrap_request['exchange_type']} activated", 
                        htmlContent=PAID_EXCHANGE\
                            .substitute({
                                "name":mailtrap_request["recipient_name"],
                                "exchange_type":mailtrap_request["exchange_type"],
                                "reference":mailtrap_request["reference"]
                            })
                    )

            mailtrap_data = {
                "email":"unitimarket@outlook.com",
                "sender":{
                        "email":"unitimarket@outlook.com",
                        "name":"Moneyswap"
                    },
                "to":[
                    {
                        "email":mail.recipient_email,
                        "name":mail.name
                    }
                ],
                "subject":mail.subject,
                "htmlContent":mail.htmlContent
            }
            post(
                "https://api.brevo.com/v3/smtp/email",
                data=dumps(mailtrap_data),
                headers={
                    "api-key":"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",
                    "content_type":"application/json",
                    "accept":"application/json"
                }
            )
        except Exception as exc:
            error_raiser(exc)


    @staticmethod
    def sendText(
        recipient_number:str,
        body: str,
        error_raiser
    ):
        try:
            return EbulkSMS.sendSMS(
                recipient_number,
                body
            )
        except Exception as exc:
            error_raiser(exc)
        