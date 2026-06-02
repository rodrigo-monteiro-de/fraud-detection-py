from kafka import KafkaConsumer
import json

from rules import (
    high_amount_rule,
    suspicious_country_rule,
    suspicious_hour_rule
)

def detect_fraud(transaction):
    rules = [
        high_amount_rule,
        suspicious_country_rule,
        suspicious_hour_rule        
        ]
        
    alerts = []
    
    for rule in rules:
        result = rule(transaction)
        
        if result:
            alerts.append(result)
            
    return

consumer = KafkaConsumer(
    "transaction-events", #topic
    bootstrap_servers="localhost:9092",
    group_id="fraud_group",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(
        x.decode("utf-8")
    )
)

print("Aguardando transações...")

for message in consumer:
    transaction = json.loads(message.value)  # kafka entrega dicionario Python
    
    print(f"\nTransação recebida {transaction}")
    
    alerts = detect_fraud(transaction)

    if alerts:
        print(f"Fraud detected:{', '.join(alerts)}")
    else:
        print("Transaction aproved")
    