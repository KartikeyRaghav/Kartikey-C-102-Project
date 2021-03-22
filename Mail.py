import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import date

today = date.today()
d1 = str(today.strftime("%d %b"))
toaddr = "kartikeyraghav2006@gmail.com"
msg = MIMEMultipart()
msg['To'] = toaddr
query = input('Whose mail you want to be sent: ')
global password
global filename

if 'j' in query:
    fromaddr = "jvmpcreation@gmail.com"
    password = 'creation@jvmp'
    msg['From'] = fromaddr
    msg['Subject'] = "Order Fulfillment Report " + d1
    body = "Dear Team\n\nPFA for the order fulfilment report of " + d1 + '.\n\n--\nThanks\n\nJVMP Creations'
    msg.attach(MIMEText(body, 'plain'))
    filename = "Order Fulfillment Report " + d1 + '.xlsx'
    attachment = open("E:\Desktop\\"+filename, "rb")
elif 'k' in query:
    fromaddr = "kktraders.2021@gmail.com"
    password = 'traderskk@123'
    msg['From'] = fromaddr
    msg['Subject'] = "Dispatch and Delivery Details " + d1
    body = "Dear Team\n\nPFA for the dispatch and delivery details of " + d1 '.\n\n--\nThanks & Regards\n\nVikas\nKK Traders'
    msg.attach(MIMEText(body, 'plain'))
    filename = "Dispatch Details " + d1 + '.xlsx'
    attachment = open("E:\Desktop\\"+filename, "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, password)
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
print('Mail Sent')
s.quit()
