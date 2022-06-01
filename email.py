# SENDING-MAIL-THROUGH-PYTHON-
//⁘You can send E-mail through python by just entering E-mail id  
import smtplib
to=input("Enter Email id")
sub=input("Enter subject")
Meg=input("Enter Message")

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("//enter email id through you want to send e-mail")

mymessage="Subject:{}\n\n{}".format(sub,Meg)

s.sendmail("your email id",to,mymessage)
s.quit()
print("Mail send succesfully ")
