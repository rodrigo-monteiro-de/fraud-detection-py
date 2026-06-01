from kafka import KafkaConsumer
import json

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
    transaction = message.value

    print("\nTransação recebida")
    print(transaction)

    if transaction["amount"] > 1000:
        print(f"Fraud detected - High amount: ${transaction['amount']}")
        
        
    if transaction.get("country") in ["RU", "KP"]:
        print(f"Fraud detected - Suspicious country: ${transaction['country']}")