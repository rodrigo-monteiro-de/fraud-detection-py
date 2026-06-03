# Fraud Detection Pipeline with Apache Kafka

## Project Overview

This project simulates a real-time fraud detection pipeline using Apache Kafka and Python.

The main goal was not only to build a fraud detection system, but also to understand the fundamentals of event-driven architectures, message streaming, and the Producer/Consumer communication model widely used in modern data platforms.

The project generates transaction events, publishes them to Kafka, consumes them in real time, and applies fraud detection rules to identify suspicious transactions.

---

## Architecture

```text
Producer (Python + Faker)
          |
          v
    Kafka Topic
(transaction-events)
          |
          v
 Fraud Consumer
          |
          v
 Fraud Detection Rules
          |
          v
 Fraud Alerts
```

---

## Technologies Used

* Python
* Apache Kafka
* Docker
* Faker
* JSON
* Git
* GitHub

---

## Features

### Producer

Generates simulated transaction events containing:

* Transaction ID
* Customer ID
* Amount
* Country
* Merchant
* Payment Method
* Transaction Hour

Example:

```json
{
  "transaction_id": 101,
  "customer_id": 875,
  "amount": 15000,
  "country": "RU",
  "merchant": "Amazon",
  "payment_method": "Credit Card",
  "hour": 2
}
```

### Consumer

Consumes transaction events from Kafka and evaluates them using fraud detection rules.

### Fraud Rules

#### High Amount Rule

Detects transactions above a configured threshold.

```python
amount > 10000
```

#### Suspicious Country Rule

Detects transactions coming from high-risk countries.

#### Suspicious Hour Rule

Detects transactions occurring during unusual hours.

```python
0 < hour <= 5
```

---

## What I Learned

This project was designed as a learning exercise to understand how event streaming systems work.

Key concepts learned:

### Apache Kafka

* Topics
* Producers
* Consumers
* Consumer Groups
* Event Streaming
* Key/Value Messages
* Message Serialization
* Event-Driven Architecture

### Python

* Modular code organization
* Functions and business rules
* JSON serialization/deserialization
* Error investigation and debugging

### Docker

* Running Kafka in containers
* Managing local development environments
* Container inspection and troubleshooting

---

## Challenges and Mistakes

One of the most valuable parts of this project was debugging real-world issues.

### Missing Return Statement

Initially, the fraud detection engine collected alerts correctly but returned nothing.

Incorrect:

```python
return
```

Correct:

```python
return alerts
```

This caused every transaction to be approved even when fraud conditions were detected.

---

### Double JSON Deserialization

I mistakenly attempted to deserialize messages twice.

Incorrect:

```python
transaction = json.loads(message.value)
```

Since KafkaConsumer was already configured with a deserializer, the message was already a Python dictionary.

Correct:

```python
transaction = message.value
```

---

### Missing Transaction Hour

A fraud rule depended on the transaction hour, but the producer was not sending that field.

This caused rule evaluation issues and reinforced the importance of schema consistency between producers and consumers.

---

### Kafka Command Troubleshooting

While testing Kafka, I learned how to:

* Access containers
* Inspect Kafka topics
* Validate broker availability
* Locate Kafka CLI tools inside Docker containers
* Verify message flow end-to-end

---

## Sample Output

Approved transaction:

```text
==================================================
Transaction ID: 125
==================================================
Transaction approved
```

Fraudulent transaction:

```text
==================================================
Transaction ID: 126
==================================================
FRAUD ALERT
- High amount: 15000
- Suspicious country: RU
- Transaction at unusual hour: 2h
```

---

## Future Improvements

Possible next steps:

* Store events in Amazon S3
* Export transactions to Parquet files
* Implement AWS Lambda integration
* Add Apache Spark processing
* Create fraud alert dashboards
* Introduce machine learning models for anomaly detection

---

## Project Goal

The purpose of this project was to gain practical experience with event-driven data pipelines and build a foundation for future Data Engineering projects involving cloud platforms and streaming architectures.

This project represents an important step in my learning journey toward becoming a Data Engineer.
