import smtplib
from email.mime.text import MIMEText


def send_email(email, height, average_height, count):
    # Set up the MIME
    from_email = 'meetvvk2@gmail.com'
    from_password = 'hfjuxfayrxyzjnsv'
    to_email = email

    subject = 'Height Data'
    message = ("Hey there, your height is <strong>%s</strong>. Average height of all is <strong>%s</strong> and that "
               "is calculated out <strong>%s</strong> of people") % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
    # Connect to Gmail's SMTP server
    # with smtplib.SMTP('smtp.gmail.com', 587) as server:
    #     server.starttls()
    #     server.login('meetvvk2@gmail.com', 'hfjuxfayrxyzjnsv')
    #
    #     # Send the email
    #     server.sendmail('meetvvk2@gmail.com', 'meetvvk@gmail.com', message.as_string())
