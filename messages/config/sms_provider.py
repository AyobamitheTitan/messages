# config/sms_provider.py

SMS_PROVIDERS = {
    'provider1': {
        'api_key': 'api_key1',
        'base_url': 'https://api.provider1.com/sms',
        'username':'Moneyswap',
        'default_sender': 'Provider1'
    },
    'provider2': {
        'username':'Moneyswap',
        'api_key': 'api_key2',
        'base_url': 'https://api.provider2.com/sms',
        'default_sender': 'Provider2'
    },
    'provider3':{
        'api_key':'e15256c7154aeaa5504207d6c28b0a6bdd2bbf29',
        'username':'dewteks@gmail.com',
        'default_sender':'Moneyswap',
        'base_url':'https://api.ebulksms.com/sendsms'
    }
}
