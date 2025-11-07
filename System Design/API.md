#### Status Codes
200 OK: Request successful, data returned.
201 Created: New resource created.
204 No Content: Success but no data returned.
400 Bad Request: Invalid request.
401 Unauthorized: Missing or invalid API key.
500 Internal Server Error: Server encountered an error.

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

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# ---- Config ----
OIDC_ISSUER = "https://your-idp.example.com"
OIDC_AUDIENCE = "orders-api"
OIDC_JWKS_URL = f"{OIDC_ISSUER}/.well-known/jwks.json"

# ---- Schema ----
class Order(BaseModel):
    order_id: constr(strip_whitespace=True, min_length=1)
    user_id: constr(strip_whitespace=True, min_length=1)
    quantity: float = Field(gt=0)
    price: Optional[float] = Field(default=None, gt=0)
    currency: str

def verify_token(auth_header: str):
    pass

# ---- Routes ----
@app.route("/api/orders", methods=["POST"])
def create_order():
    claims, err = verify_token(request.headers.get("Authorization"))
    if err:
        return jsonify({"error": err}), 401

    try:
        payload = request.get_json(force=True)
        order = Order(**payload)
    except ValidationError as ve:
        return jsonify({"error": "Validation failed", "details": ve.errors()}), 422
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # Example authorization check
    if claims.get("sub") != order.user_id:
        return jsonify({"error": "Forbidden: user mismatch"}), 403

    # For now, just acknowledge the order
    return jsonify({
        "status": "accepted",
        "order_id": order.order_id,
        "received_at": datetime.utcnow().isoformat() + "Z"
    }), 202

@app.route("/healthz", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(port=8080)
```
