from rules import (
    high_amount_rule,
    suspicious_country_rule,
    suspicious_hour_rule
)

transaction = {
    "transaction_id": 1,
    "amount": 15000,
    "country": "RU",
    "hour": 2
}

print(high_amount_rule(transaction))
print(suspicious_country_rule(transaction))
print(suspicious_hour_rule(transaction))