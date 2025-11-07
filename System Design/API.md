#### Status Codes
- 200 OK: Request successful, data returned.
- 201 Created: New resource created.
- 204 No Content: Success but no data returned.
- 400 Bad Request: Invalid request.
- 401 Unauthorized: Missing or invalid API key.
- 422 Unprocessable Content: Validation errors in content
- 500 Internal Server Error: Server encountered an error.

```python
# app.py
import logging
from datetime import datetime
from typing import Optional

from flask import Flask, request, jsonify
from authlib.jose import jwt, JsonWebToken
from authlib.jose.errors import JoseError
import requests
from pydantic import BaseModel, Field, ValidationError, constr
from confluent_kafka import Producer

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Initialize Redis cache client object
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# Initialize producer (assuming broker config is already handled)
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# ---- Schema ----
class Order(BaseModel):
    order_id: constr(strip_whitespace=True, min_length=1)
    user_id: constr(strip_whitespace=True, min_length=1)
    quantity: float = Field(gt=0)
    price: Optional[float] = Field(default=None, gt=0)
    currency: str

def verify_token(auth_header: str):
    pass

def delivery_report(err, msg):
    if err is not None:
        logger.error(f"Delivery failed: {err}")
    else:
        logger.info(f"Delivered to {msg.topic()} [{msg.partition()}]")

# ---- Routes ----
@app.route("/api/orders", methods=["POST"])
def create_order():
    claims, err = verify_token(request.headers.get("Authorization"))
    if err:
        return jsonify({"error": err}), 401

    # Validate datamodel
    try:
        payload = request.get_json(force=True)
        order = Order.parse_obj(payload)
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 422
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # Example authorization check
    if claims.get("sub") != order.user_id:
        return jsonify({"error": "Forbidden: user mismatch"}), 403

    # Idempotency: if idempotency_key provided, attempt to reuse existing order
    # Should check if content differs from original, if so respond with error code
    if order_in.idempotency_key:
        existing_id = r.get(f"idempotency:{order_in.idempotency_key}")
        if existing_id:
            existing_order = r.get(f"order:{existing_id}")
            return jsonify(json.loads(existing_order)), 200

    # Serialize validated order to JSON
    message = order.json()

    # Push onto Kafka topic
    producer.produce(
        topic="orders",
        key=order.order_id,               # partition by order_id
        value=message.encode("utf-8"),
        callback=delivery_report
    )
    producer.poll(0)  # trigger delivery

    return jsonify(order.dict()), 201

@app.route("/healthz", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(port=8080)
```
