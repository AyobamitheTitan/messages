from string import Template

ONBOARDING=Template("<html><head></head><body><h4>Hello ${name},</h4><br/><p>Welcome to Moneyswap. Use this code for your verification ${code}.</p></body></html>")
CODE=Template("<html><head></head><body><h4>Hello ${name},</h4><br/><p>Use this code to complete your ${action} : <b>${code}</b>.</p></body></html>")
PASSWORD_RESET=Template("<html><head></head><body><h4>Hello ${name},</h4><br/><p>Your password was just changed. If this wasn't you, please send us an email at help@moneyswap.com.</p></body></html>")
EXPIRED_EXCHANGE=Template("<html><head></head><body><h4>Hello ${name},</h4><br/><p>Your ${exchange_type} ${reference} has expired, and all blocked funds have been returned to your wallet. Please go back to the app to make another swap request</p></body></html>")
COMPLETED_EXCHANGE=Template("<html><head></head><body><h4>Hello ${name},</h4><br/><p>Your ${exchange_type} ${reference} has been successfully completed and closed, and your wallet has been funded successfully. Please go back to the app to make another swap request</p></body></html>")
PAID_EXCHANGE=Template("<html><head></head><body><h4>Hello ${name},</h4><br/><p>Your ${exchange_type} ${reference} has been successfully activated and your wallet has been debited</p></body></html>")
PROFILE_CHANGE=Template("<html><head></head><body><h4>Hello ${name},</h4>. Your ${profile_entity} is about to be changed. If you did not initiate this process, please send us an email at help@moneyswap.com.</body></html>")