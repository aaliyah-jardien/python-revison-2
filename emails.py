# IMPORTING SMTP LIBRARY
import smtplib

x = smtplib.SMTP("smtp.gmail.com", 587)

# declare your email, and the sender, and your password
my_email_address = "aaliyahjar13@gmail.com"
receiver_address = "mndabeni6@gmail.com"
password = input("Please enter password: ")

x.starttls()
x.login(my_email_address, password)

message = "You are Marvellous."

x.sendmail(my_email_address, receiver_address, message)
x.quit()
