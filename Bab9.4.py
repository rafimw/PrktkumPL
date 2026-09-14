import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = "rafifrafimuzakkiwidodo@gmail.com"
toaddr = "rafifrafimw@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "TEST TEKS OTOMATIS"
body = '''Test woiiiii'''
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "#####") #Passwordnya ngap
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
