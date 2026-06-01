from kafka import KafkaProducer
from faker import Faker
import json
import time
import random

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v:json.dumps(v).encode("utf-8")
)

countries = [
    "BR",
    "US",
    "AR",
    "RU",
    "KP"
]

merchants = [
    "Amazon",
    "Mercado Livre",
    "Magalu",
    "Steam",
    "Netflix"
]

payment_methods = [
    "CREDIT_CARD",
    "PIX",
    "DEBIT_CARD"
]

contador = 1

while True:
    
    evento = {
        "transaction_id": contador,
        "customer_id":random.randint(1,1000),
        "amount":random.randint(100,20000),
        "country":random.choice(countries),
        "merchant":random.choice(merchants),
        "payment_methods":random.choice(payment_methods)
    }
    
    producer.send(
        
        "transaction-events",
        evento
    )
    
    print(f"Enviado: {evento}")
    contador +=1 
    time.sleep(2)
    