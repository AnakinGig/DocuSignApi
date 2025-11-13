from flask import Blueprint, request, jsonify
from .docusign_client import DocuSignClient
from docusign_esign.client.api_exception import ApiException
import json, logging, base64

logging.basicConfig(level=logging.INFO)
api_bp = Blueprint("api", __name__)

@api_bp.route("/send-pdf", methods=["POST"])
def send_pdf():
  try:
    # File sent
    data = request.form
    logging.info('Received data')
    file = request.files.get("file")
    logging.info('Received file')
    
    if not file:
      return jsonify({"error": "No file uploaded"}), 400

    # Credentials & user info
    integrator_key = data.get("integrator_key")
    account_id = data.get("account_id")
    user_id = data.get("user_id")
    private_key = base64.b64decode(data.get("private_key_b64")).decode("utf-8")
    client_email = data.get("email")
    client_name = data.get("name")

    logging.info('Received credentials')
    
    if not all([integrator_key, account_id, user_id, private_key, client_email, client_name]):
      return jsonify({"error": "Missing required fields"}), 400

    client = DocuSignClient(integrator_key, account_id, user_id, private_key)
    envelope_summary = client.send_document(client_email, client_name, file.read(), file.filename)

    return jsonify({"envelope_id": envelope_summary.envelope_id}), 200
  
  # Catch error of the API
  except ApiException as e:
    body = e.body.decode('utf-8')
    try:
      body = json.loads(body)
    except json.JSONDecodeError:
      pass
    logging.info(e)
    return jsonify({
      "error": "Docusign API Error",
      "reason": e.reason,
      "body": body,
      "headers": dict(e.headers)
    }), 500
  except Exception as e : 
    logging.info(e)
    return jsonify({"error" : e})