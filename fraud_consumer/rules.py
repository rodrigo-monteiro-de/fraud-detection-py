def high_amount_rule(transaction):
    if transaction["amount"] > 10000:
        return f"High amount: {transaction['amount']}"
        
    return None

def suspicious_country_rule(transaction):
    if transaction["country"] not in ["BR","US"]:
        return f"Suspicious country: {transaction['country']}"
        
    
    return None
    
def suspicious_hour_rule(transaction):
    if transaction["hour"] > 0 and transaction["hour"] <= 5:
        return f"Transaction at unusual hour: {transaction['hour']}h"
    
    return None
        
