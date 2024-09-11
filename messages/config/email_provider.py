# config/email_provider.py
from typing import Any, Dict
EMAIL_PROVIDERS: Dict[str, Dict[str,Any]] = {
    'provider1': {
        'host': 'live.smtp.mailtrap.io',
        'port': 587,
        'username': 'api',
        'password': '1bad36257c671e55835cf52e40a9d10a',
        'use_tls': True,
        'sender':'mailtrap@marketz.live'
    },
    'provider2': {
        'host': 'smtp.provider2.com',
        'port': 587,
        'username': 'user2@example.com',
        'password': 'password2',
        'use_tls': True,
        'sender':"45@536.cgo"
    },
    'provider3':{
        'host':'smtp-relay.brevo.com',
        'port':587,
        'username':'unitimarket@outlook.com',
        'password':'sOk1YNQdJq3SBHyx',
        'use_tls':True,
        'sender':'Moneyswap'
    }
    # Add more providers as needed
}

TEXT_PROVIDER : Dict[str, Dict[str,str]] = {
    'provider1':{
        'from_':'+13133519053',
        'account_sid':'AC1bf3ca6c0c7ea921a3aaaf76200fb2b3',
        'auth_token':'8aa89dfb910670d01fbdd5642dfb27f8'
    }
}



        