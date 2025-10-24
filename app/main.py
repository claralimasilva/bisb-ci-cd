from flask import Flask, jsonify, request
from .utils import average_ticket

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/metrics/average-ticket", methods=["POST"])
def metrics_average_ticket():
    """
    Expected JSON body:
    {
        "services": [
            {"price": 120.0},
            {"price": 80.0},
            {"price": 100.0}
        ]
    }
    """
    data = request.get_json(silent=True) or {}
    services = data.get("services", [])

    try:
        value = average_ticket(services)
        return jsonify({"average_ticket": value}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# optional: only runs when doing `python main.py` locally
if __name__ == "__main__":
    app.run(debug=True)
