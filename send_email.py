import logging
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import env

SMTP_HOST = getattr(env, 'SMTP_HOST')
SMTP_PORT = getattr(env, 'SMTP_PORT')
SMTP_PASSWORD = getattr(env, 'SMTP_PASSWORD')
SMTP_USERNAME = getattr(env, 'SMTP_USERNAME')

email_list = ['email@example.com',
              'firstname.lastname@example.com',
              'email@subdomain.example.com',
              'firstname+lastname@example.com',
              'email@123.123.123.123',
              'email@[123.123.123.123]',
              '"email"@example.com',
              '1234567890@example.com',
              'email@example-one.com',
              '_______@example.com',
              'email@example.name',
              'email@example.museum',
              'email@example.co.jp',
              'firstname-lastname@example.com',
              '@%^%#$@#$@#.com',
              '@example.com',
              'Joe Smith <email@example.com>',
              'email.example.com',
              'email@example',
              '.email@example.com',
              'email.@example.com',
              'email..email@example.com',
              'あいうえお@example.com',
              'email@example.com (Joe Smith)',
              'email@example',
              'email@-example.com',
              'email@example.web',
              'email@111.222.333.44444',
              'email@example..com',
              'abc..123@example.com',
              ',,@gmail.com']

my_email = 'khusbuthapa13@gmail.com'

logging.basicConfig(filename='app.log', filemode='a+', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)


def check_email(email):
    valid_email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    return True if re.match(valid_email_regex, email) else False


def send_email(emails):
    import smtplib

    host = SMTP_HOST
    port = SMTP_PORT
    password = SMTP_PASSWORD
    sender_email = SMTP_USERNAME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = 'khusbuthapa13@gmail.com'
    msg['Subject'] = 'Test Email'
    content = """
    <html>
    <head></head>
    <body style="color:black;">
    <p>Hello Dear,</p>
    <p>
    Please find this email as the notification that your email has been verified.
    </p>
    <p>
    Regards,
    <br>
    Khushbu Thapa
    </p>
    </body>
    </html>
    """

    part2 = MIMEText(content, 'html')
    msg.attach(part2)

    # Default values
    result = None
    recipient_emails = []

    if emails:
        to_email = emails.pop()
        recipient_emails = [to_email]
    cc = emails
    recipient_emails += cc

    if recipient_emails:
        with smtplib.SMTP(host, port) as server:
            server.login(sender_email, password)
            try:
                result = server.sendmail(sender_email, recipient_emails, msg.as_string())
            except Exception as error:
                logging.warning(f'{error}')
            server.quit()
    return result


def process_emails(emails=email_list):
    valid_emails = list(filter(check_email, emails))
    invalid_emails = [email for email in emails if email not in valid_emails]

    logging.warning(f'Invalid Emails: {invalid_emails}')

    result = send_email(valid_emails)
    if result is {}:
        logging.info(f'Email sent to: {valid_emails}')
        print("Emails sent successfully!")
        return "Emails sent successfully!"
    else:
        return "Couldn't send even a single email."


if __name__ == "__main__":
    process_emails()
