from requests import request

class EbulkSMS:
    @staticmethod
    def sendSMS(recipient_number: str, body: str, error_raiser, SMS_PROVIDERS:dict):
        try:
            #TODO: Maybe give this it's own config? Not sure.
            USERNAME = SMS_PROVIDERS.get('provider3').get('username')
            SENDER = SMS_PROVIDERS.get('provider3').get('default_sender')
            API_KEY = SMS_PROVIDERS.get('provider3').get('api_key')
            BASE_URL = SMS_PROVIDERS.get('provider3').get('base_url')
            response = request(
                "GET",
                url=f"{BASE_URL}?username={USERNAME}&apikey={API_KEY}&sender={SENDER}&messagetext={body}&flash=0&recipients={recipient_number}"
            )
            return response.text
        except Exception as exc:
            error_raiser(exc)