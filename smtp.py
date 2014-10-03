import smtplib

def send_email(user_name, pwd):
	gmail_user = user_name
	gmail_pwd = pwd
	FROM = 'mail_alrt@gmail.com' #Not working, will alway use user account and password.
	TO = ['evanslin@gmail.com'] #must be a list, send email to self
	SUBJECT = "Testing sending using gmail"
	TEXT = "Testing sending mail using gmail servers"

	# Prepare actual message
	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	try:
	    server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
	    server.ehlo()
	    server.starttls()
	    server.ehlo()
	    server.login(gmail_user, gmail_pwd)
	    server.sendmail(FROM, TO, message)
	    #server.quit()
	    server.close()
	    print 'successfully sent the mail'
	except:
	    print "failed to send mail"

gmail_account = raw_input("Please enter Gmail Account: ")
gmail_pw = raw_input("Please enter Gmail Password: ")
send_email(gmail_account, gmail_pw)

