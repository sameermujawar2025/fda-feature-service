# fraud-precheck-service
Entry point for all transactions. Performs initial data validation and routing to the Rule Engine. Part of the Fraud Detection Platform.

# 🧭 Fraud Precheck Service

The **Fraud Precheck Service** is the **entry point** of the [Fraud Detection Platform](https://github.com/fraud-detection-platform).  
It receives transaction requests, performs validations, enriches input data, and routes clean transactions to the **Rule Engine Service** for fraud scoring.

---

## ⚙️ Key Responsibilities

- Validate incoming transaction payloads
- Perform lightweight risk checks (e.g., missing fields, merchant status)
- Log all requests with correlation IDs
- Forward valid transactions to **Rule Engine Service**

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| Language | Java 21 |
| Framework | Spring Boot 3.4.4 |
| Build Tool | Maven |
| Containerization | Docker |
| Communication | REST APIs |

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/api/v1/precheck` | `POST` | Validate transaction and forward to Rule Engine |

### Example Request
```json
{
  "transaction": { "txn_id":"...", "amount": 250.0, "merchant_id": "M123", "timestamp":"...", "payment_method":"WALLET", "lat":..., "lon":... },
  "rule_features": { "velocity_count": 4, "is_night": true, "geo_speed_kmh": 1200 },
  "client_id": "tenant_abc"
}

