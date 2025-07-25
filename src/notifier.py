import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Advert import Advert

def send_email(subject, body, recipients, credentials):

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = credentials["email"]
    msg['To'] = recipients[0]
    msg['Subject'] = subject
    
    if len(recipients) > 1:
        msg['Cc'] = ", ".join(recipients[1:]) # Join multiple CC emails with a comma and space


    # Attach the email body
    msg.attach(MIMEText(body, 'html'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(credentials["email"], credentials["password"])

        # Send the email
        server.sendmail(credentials["email"], recipients[0], msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

def notify(new_adverts, recipients, credentials):
    details = ""
    for advert in new_adverts:
        advert: Advert = advert
        details += f"<li><a href=\"{advert.page_url}\">{advert.page_url}</a>"
        if advert.title:
            details += f"<p>{advert.title}</p>"
        details += "</li>"
    html = f"""\
        <html>
        <body> 
            <p>New adverts:</p>
            <ul>
            {details}
            </ul>
        </body>
        </html>
        """
    send_email("New Housing Adverts!", html, recipients, credentials)
    