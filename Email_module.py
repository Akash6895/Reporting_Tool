"""
This Module works with 'Sendinblue' Website Account
User: Akashtaralkar@outlook.com
Pw: Akash@123
API Key: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
You can find the template projects on the websites
"""

from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


def send_email(message, to, fromm):
    configuration = sib_api_v3_sdk.Configuration()
    api_key = "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"
    configuration.api_key['api-key'] = api_key

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    # Type The Subject Here
    subject = "from the Python SDK!"

    # Type the Sender Email ID
    sender = {"name": "Akash Python Script", "email": f"{fromm}"}

    # Type Reply to Email ID
    replyTo = {"name": "Sendinblue", "email": f"{fromm}"}

    # Type HTML Message body
    html_content = f"<html><body><h1>{message}</h1></body></html>"

    # Type receivers email ID and Name
    to = [{"email": f"{to}", "name": "Akash Taralkar"}]
    params = {"parameter": "My param value", "subject": "New Subject"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, reply_to=replyTo,
                                                   html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        # print(api_response)
        return 0
    except ApiException as e:
        # print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
        return str(e), -1
