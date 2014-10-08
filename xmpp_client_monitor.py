# -*- coding: utf-8 -*-
# xmpppy
# http://xmpppy.sourceforge.net/
import xmpp
import random
import struct
import sys
import datetime

reload(sys)
sys.setdefaultencoding("utf-8")

import smtplib

def send_email(user_name, pwd):
    gmail_user = user_name
    gmail_pwd = pwd
    FROM = 'mail_alrt@gmail.com' #Not working, will alway use user account and password.
    TO = ['Email Test'] #must be a list, send email to self
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

class Bot:
    """ Jabber Bot Base Class """
    JID = ''
    PASSWORD = ''
    client = None   
    Targe_ID = ''

    def __init__ (self, jid, password):
        self.JID = xmpp.JID(jid)
        self.PASSWORD = password
        self.login()

    def login (self):
        self.client = xmpp.Client(server=self.JID.getDomain(), port=80, debug=[])
        if self.client.connect() == '':
            raise 'JabberBot not connected.'
        if self.client.auth(self.JID.getNode(), self.PASSWORD) == None:
            raise 'JabberBot authentication failed.'
        
        self.client.RegisterHandler('message', self.message_callback)
        self.client.RegisterHandler('presence', self.presence_callback)
        self.client.sendInitPresence()
        print 'completed login in host', self.JID.getDomain() ,' wait message...'

    def message_callback (self, client, message):
        print 'coming message:', message

    def presence_callback (self, client, message):
        #print 'presence change.....'
        type = message.getType()
        who = message.getFrom().getStripped()

        if type == 'subscribe':
            self.subscribe(who)
        elif type == 'unsubscribe':
            self.unsubscribe(who)
        elif type == 'subscribed':
            self.subscribed(who)
        elif type == 'unsubscribed':
            self.unsubscribed(who)
        elif type == 'available' or type == None:
            self.available(message)
        elif type == 'unavailable':
            self.unavailable(who)

    def subscribe (self, jid):
        """ 加好友 """
        self.client.send(xmpp.Presence(to=jid, typ='subscribed'))
        self.client.send(xmpp.Presence(to=jid, typ='subscribe'))

    def unsubscribe (self, jid):
        """ 取消好友 """
        self.client.send(xmpp.Presence(to=jid, typ='unsubscribe'))
        self.client.send(xmpp.Presence(to=jid, typ='unsubscribed'))

    def subscribed (self, jid):
        """ 已加 """

    def unsubscribed (self, jid):
        """ 已退 """
        
    def available (self, message):
        """ 上線 """

    def unavailable (self, jid):
        """ 下線 """

    def send (self, jid, message):
        """ 發消息給某人"""
        self.client.send(xmpp.protocol.Message(jid, message))

    def step (self):
        """ 用在迴圈中 """
        try:
            self.client.Process(1)
        except KeyboardInterrupt:   # Ctrl+C停止
            return False
        return True
    def addTarget(self, target_jid):
        self.Targe_ID = target_jid

class Bot(Bot):
    def message_callback (self, cl, msg):
        fromid = msg.getFrom().getStripped()
        cont = msg.getBody()
        if 'dainty' in fromid: 
            print 'self call...'
        else:
            current_time = datetime.datetime.now()
            #send notify to self to prevent timeout.
            self.send('ID', "ALive")
            print 'send message to evan'
            print current_time, 'coming message:', cont, 'from: ', fromid

    def get_random_string(self, range):
        return_string = struct.pack('<Q', random.randint(1, range))
        return_string.encode('hex')

if __name__ == '__main__':
    gmail_account = raw_input("Please enter notify Gmail Account: ")
    gmail_pw = raw_input("Please enter notify Gmail Password: ")
    #send_email(gmail_account, gmail_pw)

    use_test_server = True
    gb = Bot ('ID', 'PWD')

    # 開始運行
    while (gb.step()): pass
