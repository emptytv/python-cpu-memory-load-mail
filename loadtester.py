# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import psutil
import socket

max_cpu_percent = 50
max_memory_percent = 50
def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"




print(psutil.cpu_times())

# CPU Usage
print(psutil.cpu_percent(interval=1))
cpu_percent = psutil.cpu_percent(interval=1)
if(cpu_percent > max_cpu_percent):
    print("Warning")
    print("CPU Usage Greter than 50%")
    #print (str(socket.gethostname()))
    # @type mem 
    send_email('example@gmail.com', '*****', 'to@gmail.com', 'Memory Usage High for someIP', 'The current memory usage for someIP is '+ str(mem.percent))

# Memory Usage
print(psutil.virtual_memory())
mem =  psutil.virtual_memory()

print("Memory Percent="+str(mem.percent))
if(mem.percent > max_memory_percent):
    print("Memory Usage Greter than 50%")
    #print (str(socket.gethostname()))
    # @type mem 
    send_email('example@gmail.com', '*****', 'to@gmail.com', 'Memory Usage High for someIP', 'The current memory usage for someIP is '+ str(mem.percent))
