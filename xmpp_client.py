# -*- coding: utf-8 -*-

#Python語言: python gtalk機器人
# coding: utf-8
# 這是根據xmpp封裝的Jabber聊天機器人類, 可以通過繼承,重載部分函數來自定義功能.
# Jabber ID(JID): 比如gamcat@gmail.com
import xmpp
import random
import struct
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

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
        self.client = xmpp.Client(self.JID.getDomain(), port=80, debug=[])
        if self.client.connect() == '':
            raise 'JabberBot not connected.'
        if self.client.auth(self.JID.getNode(), self.PASSWORD) == None:
            raise 'JabberBot authentication failed.'
        
        self.client.RegisterHandler('message', self.message_callback)
        self.client.RegisterHandler('presence', self.presence_callback)
        self.client.sendInitPresence()

    def message_callback (self, client, message):
        """ 默認消息回調(可通過繼承自定義) """
        print 'coming message:', message

    def presence_callback (self, client, message):
        """ 默認事件回調,包括下面幾個(可通過承自定義) """
        print 'login.....'
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

#===========================
# 測試
#===========================
class Bot(Bot):
    def message_callback (self, cl, msg):
        fromid = msg.getFrom().getStripped()
        cont = msg.getBody()
        #self.send2admin(msg)
        print 'coming message:', cont

        message_out = ''
        if 'GetDeviceList' in cont:
            message_out = 'DeviceList:{003};{BDA1-ACFFFFFCC9927};{FF000000};{BDA2-BCFFFFFCC9927};{8F000000};{BDA3-CCFFFFFCC9927};{80000000};'
            self.send(self.Targe_ID, message_out)
            
        elif  'Read' in cont:
            message_out = 'Data:{BDA1-ACFFFFFCC9927};{{E32300}{E55000}{A2F41000000000}{9AF420000000}{99110000}{1010}{C1RSSI0000}{C2120000}{C30100}{C4}{C51A2B}}'
            self.send(self.Targe_ID, message_out)
        print 'sending message:', message_out

    def send2admin (self, message):
        #self.send('admin@gmail.com', 'Test')
        print 'send2admin'

    def get_random_string(self, range):
        return_string = struct.pack('<Q', random.randint(1, range))
        return_string.encode('hex')

if __name__ == '__main__':
    gb = Bot ('test1@xmpp-server1', '1234')
    gb.send2admin ('Bot Started')
    gb.addTarget('test2@xmpp-server1')
    # 開始運行
    while (gb.step()): pass
