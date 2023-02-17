import smtplib

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com',
    'gmail': '@gmail.com',
    'live': '@live.com'
}

def send(message):
    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_mail = 'tfroh{}'.format(carriers['live'])
    auth = ('tfroh3@gmail.com', 'pxopydtefmshpomc')

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(auth[0], auth[1])
    print(to_mail)


    # Send text message through SMS gateway of destination number
    err = server.sendmail( auth[0], to_mail, message)
    print(err)

    server.close()