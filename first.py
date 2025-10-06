print("RAM")
# import webbrowser
# import time

# # Base URL format
# base_url = "https://www.hs-aalen.de/en/courses/{}/staff"

# # Open all URLs from 21 to 100
# for course_id in range(151, 200):
#     url = base_url.format(course_id)
#     webbrowser.open_new_tab(url)
#     time.sleep(0.01)  # small delay to avoid overwhelming the browser


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# Email details
sender_email = "tusharkhari57@gmail.com"
receiver_email = "tusharkhari9@gmail.com"
password = "xziu ruwe hhzd pcqf"  # Be careful with storing passwords!

subject = "Test Email from Python"
body = "Hello! This is a test email sent from Python 2."

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the body text
msg.attach(MIMEText(body, 'plain'))

# Connect to the Gmail SMTP server and send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # 587 is the TLS port
    server.starttls()  # Secure the connection
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Something went wrong: {e}")
finally:
    server.quit()
