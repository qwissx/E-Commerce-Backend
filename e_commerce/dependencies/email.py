from email.message import EmailMessage

from pydantic import EmailStr

from e_commerce import settings as st


def create_register_confirmation_template(email_to: EmailStr):
    email = EmailMessage()

    email["Subject"] = "Удостоверение регистрации"
    email["From"] = st.smtp_user
    email["To"] = email_to

    email.set_content(
        """
        <h1>Удостоверение регистрации</h1>
        Ваша почта была зарегестрирована на сайте E-Commerce
        """,
        subtype="html"
    )
    return email
