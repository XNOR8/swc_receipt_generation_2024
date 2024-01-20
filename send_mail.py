import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

sender = "cse2020067@rcciit.org.in"
password = os.environ.get("GMAIL_PASSWORD")


def send_mail(
    cc_recipients,
    recipients,
    recipient_name,
    event_name,
    registration_fees,
    created_at,
    transaction_id,
):
    recipients = [recipients]
    cc_recipients = [cc_recipients]
    cc_recipients.append("iamtridibes@gmail.com")

    body = f"""
      <div style="font-family: 'Roboto Mono', monospace; background-color: white; margin: 16px;">
         <div style="text-align: center;">
            <img src="https://imgur.com/flD82jv.png" alt="rcciit logo" height="50px" />
            <h2>RCC INSTITUTE OF INFORMATION TECHNOLOGY</h2>
            <div style="width: 100%; margin: 0 auto;">
               <img src="https://imgur.com/Yyp9O1z.png" alt="swc logo" height="50px" style="padding-right: 10px;">
               <img src="https://imgur.com/SFEbNdx.png" alt="got logo" height="50px" style="padding-left: 10px;">
            </div>
            <br />
            <h2>Game of Thrones 2024</h2>
            <h8 style="font-weight: 800; text-decoration: underline;">MONEY RECEIPT</h8>
         </div>
         <div style="padding-left: 10px; padding-right: 10px; margin-top: 20px; text-align: center;">
            <p style="margin: 0 auto;">
               Received with thanks from&nbsp;<span style="font-size: 18px; text-decoration: underline;">{recipient_name}</span>
            </p>
            <p style="margin: 0 auto;">
               on account of&nbsp;<span style="font-size: 18px; text-decoration: underline;">{event_name}</span>
            </p>
            <p style="margin: 0 auto;">
               Rs.&nbsp;<span style="font-size: 18px; text-decoration: underline;">{registration_fees}</span>
            </p>
            <p style="margin: 0 auto;">
               by Cash/UPI(Transaction Number&nbsp;<span style="font-size: 18px; text-decoration: underline;">{transaction_id}</span>)
            </p>
            <p style="margin: 0 auto;">
               on&nbsp;<span style="font-size: 18px; text-decoration: underline;">{datetime.fromisoformat(created_at).date()}</span>
            </p>
            <br/>
            <p style="font-size: 10px; color: #808080; margin: 0 auto;">Regards,<br/>Shourya Shikhar Ghosh<br/>On behalf of the G.O.T. organising committee</p>
            <br/><br/>
            <p style="font-size: 10px; margin: 0 auto;">THIS IS A SYSTEM GENERATED RECEIPT. NO SIGNATURE REQUIRED.</p>
         </div>
      </div>
    """

    msg = MIMEText(body, "html")
    msg["Subject"] = "Game of Thrones 2024 - Thank you for your participation!"
    msg["From"] = sender
    msg["To"] = ",".join(recipients)
    msg["Cc"] = ",".join(cc_recipients)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(sender, password)
        recipients += cc_recipients
        smtp_server.send_message(msg)
