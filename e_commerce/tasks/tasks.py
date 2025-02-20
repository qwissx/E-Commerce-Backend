import smtplib

from pydantic import EmailStr

from e_commerce.connections import broker
from e_commerce.dependencies.email import create_register_confirmation_template
from e_commerce import settings as st


@broker.task
def send_confirmation_email(email_to: EmailStr):
    msg_content = create_register_confirmation_template(email_to)

    with smtplib.SMTP_SSL(st.smtp_host, st.smtp_port) as server:
        server.login(st.smtp_user, st.smtp_pass)
        server.send_message(msg_content)
