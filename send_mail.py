import smtplib 
from email.mime.text import MIMEText 

def send_mail(reviewer,movie,rating,comments):
    port=2525 
    smtplib_server = 'smtp.mailtrap.io'
    login = 'YOUR_MAILTRAP_LOGIN'
    password = 'YOUR_MAILTRAP_PASSWORD'
    message = f"<h3>New Review Submission</h3><ul><li>Movie:{movie}</li><li>Rating:{rating}</li><li>Comments:{comments}</li></ul>"

    sender_email  = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message,'html')
    msg['Subject'] = 'Cineaddict Review'
    msg['From'] = sender_email 
    msg['To'] = receiver_email

    #Send email 
    with smtplib.SMTP(smtplib_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

