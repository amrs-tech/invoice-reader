import smtplib
import os
from email.message import EmailMessage

def send_email(recipient, file_path):
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    # print('emailauth==>',EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    msg = EmailMessage()
    msg['Subject'] = 'Extracted Text Document'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient
    msg.set_content("Please find the extracted text document attached.")
    
    with open(file_path, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype='application',
            subtype='octet-stream',
            filename=os.path.basename(file_path),
            disposition='inline'
        )
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
