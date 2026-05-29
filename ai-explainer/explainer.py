import os
import json
import logging
from flask import Flask, request, jsonify
from openai import OpenAI
import requests

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
SLACK_WEBHOOK = os.environ["SLACK_WEBHOOK_URL"]

SYSTEM_PROMPT = """You are a concise Kubernetes security expert.
You receive raw Falco security alerts and explain them in plain English.

Respond with ONLY a JSON object:
{
  "what_happened": "1-2 sentence plain English explanation",
  "why_it_matters": "1 sentence on the security risk",
  "immediate_action": "1 specific thing to do right now",
  "mitre_technique": "e.g. T1496 Resource Hijacking",
  "severity_emoji": "🔴 Critical, 🟠 Error, 🟡 Warning"
}"""


def explain_alert(alert: dict) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Explain:\n{json.dumps(alert, indent=2)}"}
        ],
        response_format={"type": "json_object"},
        temperature=0.1,
        max_tokens=300,
        timeout=10
    )
    return json.loads(response.choices[0].message.content)


def post_to_slack(alert: dict, explanation: dict) -> None:
    rule = alert.get("rule", "Unknown")
    priority = alert.get("priority", "unknown")
    pod = alert.get("output_fields", {}).get("k8s.pod.name", "unknown")
    ns = alert.get("output_fields", {}).get("k8s.ns.name", "unknown")
    node = alert.get("output_fields", {}).get("k8s.node.name", "unknown")
    emoji = explanation.get("severity_emoji", "🟡")

    payload = {
        "blocks": [
            {
                "type": "header",
                "text": {"type": "plain_text", "text": f"{emoji} Falco: {rule}"}
            },
            {
                "type": "section",
                "fields": [
                    {"type": "mrkdwn", "text": f"*Pod:*\n{pod}"},
                    {"type": "mrkdwn", "text": f"*Namespace:*\n{ns}"},
                    {"type": "mrkdwn", "text": f"*Node:*\n{node}"},
                    {"type": "mrkdwn", "text": f"*Priority:*\n{priority}"}
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        f"*What happened:*\n{explanation['what_happened']}\n\n"
                        f"*Why it matters:*\n{explanation['why_it_matters']}\n\n"
                        f"*Immediate action:*\n{explanation['immediate_action']}\n\n"
                        f"*MITRE:* {explanation['mitre_technique']}"
                    )
                }
            }
        ]
    }
    requests.post(SLACK_WEBHOOK, json=payload, timeout=5)


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        alert = request.get_json()
        if not alert:
            return jsonify({"error": "No JSON"}), 400
        priority = alert.get("priority", "").lower()
        if priority not in ["critical", "error", "warning"]:
            return jsonify({"status": "skipped"}), 200
        explanation = explain_alert(alert)
        post_to_slack(alert, explanation)
        return jsonify({"status": "ok", "explanation": explanation}), 200
    except Exception as e:
        logger.exception(e)
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
