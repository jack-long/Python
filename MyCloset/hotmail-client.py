
print "----- Hotmail Client -----"
promt = '''
To read email, enter 'r'.
To send email, enter 's'.
To quit, enter 'q'.
'''

def send():
    import smtplib 
    import email

    # Hotmail or Windows Live Login Information
    username = raw_input('\nWhat is your Hotmail Username?  ')
    password = raw_input('What is your Hotmail Password?  ')
    
    #connect to server
    print "Server connecting..."
    server = smtplib.SMTP('smtp.live.com:587')  
    server.starttls()
    server.login(username, password)

    toaddrs  = raw_input('Who do you want to send this to?  ')
    title = raw_input('Your message title:  ')
    content = raw_input('Type your one-line message here:\n \n    ')

    print 'Sending...'
    msg = email.message_from_string(content)
    msg['From'] = username
    msg['To'] = toaddrs
    msg['Subject'] = title
    server.sendmail(username, toaddrs, msg.as_string())

    print "Sent!"

    server.quit()
    print "Log Out"
    
def read():
    import poplib
    
    account = raw_input("input your hotmail account here (full account):")
    password = raw_input("input the password here:")

    print "Connecting..." 
    connect = poplib.POP3_SSL('pop3.live.com',995)
    connect.user(account)
    connect.pass_(password)
    numMessage=connect.stat()[0]

    #for i in range(numMessage):
    print "Reading the last mail now..." 
    for line in connect.retr(numMessage)[1]:
        print line
    connect.quit()


while True:
    print promt
    option = raw_input('What do you want? ')
    option = option.lower()
    if option == 'r':
        read()
    elif option == 's':
        send()
    elif option == 'q':
        break

print "Bye!\n"
quit