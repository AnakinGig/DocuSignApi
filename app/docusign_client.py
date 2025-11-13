from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Document, Signer, SignHere, Tabs, Recipients
import base64

class DocuSignClient:
  def __init__(self, integrator_key, account_id, user_id, private_key, environment="demo"):
    """
    integrator_key: DocuSign Integration Key (client_id)
    account_id: DocuSign account ID
    user_id: User GUID
    private_key: RSA private key string
    environment: "demo" or "production"

    NOTE: For JWT authentication, the user (user_id) must grant consent to the application.
    This is a one-time setup. More info: https://developers.docusign.com/platform/auth/jwt/jwt-grant/
    """
    self.client = ApiClient()
    self.client.set_oauth_host_name("account-d.docusign.com" if environment=="demo" else "account.docusign.com")
    self.client.set_base_path("https://demo.docusign.net/restapi" if environment=="demo" else "https://www.docusign.net/restapi")
    self.token = self.client.request_jwt_user_token(
      client_id=integrator_key,
      user_id=user_id,
      oauth_host_name="account-d.docusign.com" if environment=="demo" else "account.docusign.com",
      private_key_bytes=private_key.encode("utf-8"),
      expires_in=3600,
      scopes=["signature", "impersonation"]
    )
    self.client.set_default_header("Authorization", f"Bearer {self.token.access_token}")
    self.account_id = account_id

  def send_document(self, email, name, pdf_bytes, file_name="document.pdf"):
    # Convert PDF to base64
    file_content = base64.b64encode(pdf_bytes).decode("utf-8")

    document = Document(
      document_base64=file_content,
      name=file_name,
      file_extension="pdf",
      document_id="1"
    )

    signer = Signer(
      email=email,
      name=name,
      recipient_id="1",
      routing_order="1"
    )

    sign_here = SignHere(
      anchor_string="/sig/",
      anchor_units="pixels",
      anchor_x_offset="0",
      anchor_y_offset="0"
    )

    signer.tabs = Tabs(sign_here_tabs=[sign_here])
    recipients = Recipients(signers=[signer])

    envelope_definition = EnvelopeDefinition(
      email_subject="Veuillez signer ce document.",
      documents=[document],
      recipients=recipients,
      status="sent"
    )

    envelopes_api = EnvelopesApi(self.client)
    envelope_summary = envelopes_api.create_envelope(self.account_id, envelope_definition=envelope_definition)
    return envelope_summary