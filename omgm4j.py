#!usr/bin/python
# coding: utf-8

import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.web
import time
import hashlib

from tornado.options import define,options

WELCOME_REPLY = ''' 感谢您关注 OMG面试君 快快与我们一起备战即将来临的IT面试吧\n1.面试经验贴\n2.面试真题模拟'''

class WeixinHelper:
    def __init__(self):
        pass

    def chkauthor(self,signature,timestamp,nonce,echostr):
        #signature  = self.get_argument("signature",None)
        #timestamp = self.get_argument("timestamp",None)
        #nonce = self.get_argument("nonce",None)
        #echostr = self.get_argument("echostr",None)
        token = 'omgm4j'

        if signature and timestamp and nonce:
            params = [token,timestamp,nonce]
            params.sort()
            sha = hashlib.sha1("%s%s%s" %tuple(params)).hexdigest()
            if sha == signature:
                if echostr:
                    return echostr
                else:
                    return True
            else:
                return False
        else:
            return False

class WeixinMessage:
    def __init__(self,xmlString):
        root = ET.fromstring(text=xmlString)
        self.ToUserName = root.find('ToUserName').text
        self.FromUserName = root.find('FromUserName').text
        self.CreateTime = root.find('CreateTime').text
        self.MsgType = root.find('MsgType').text

        if self.MsgType == 'event':
            self.Event = root.find('Event').text
            if len(root.find('EventKey')) and len(root.find('Ticket')):
                #scan and subscrible event
                self.EventKey = root.find('EventKey').text
                self.EventKey = root.find('Ticket').text
            if self.Event == "LOCATION":
                #location push event
                self.Latitude = root.find('Latitude').text
                self.Longitude = root.find('Longitude').text
                self.Precision = root.find('Precision').text
        elif self.MsgType == 'image':
            pass
        elif self.MsgType == 'text':
            pass
        elif self.MsgType == 'image':
            pass
        elif self.MsgType == 'link':
            pass
        elif self.MsgType == 'location':
            pass

define("port",default=8888,help="run on the given port",type=int)
define("mysql_host",default="localhost",help="omgm4j database host")
define("mysql_database",default="test",help="omgm4j database name")
define("mysql_user",default="root",help="omgm4j database user")
define("mysql_password",default="root",help="omgm4j database password")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                (r"/",IndexHandler),
        ]
        settings = dict(debug=True,)

        tornado.web.Application.__init__(self,handlers,**settings)

        #global connection to the blog DB across handlers
        self.db = torndb.Connection(
                host=options.mysql_host,database=options.mysql_database,
                user=options.mysql_user,password=options.mysql_password,
                )

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        wxhelper = WeixinHelper()
        self.write(str(wxhelper.chkauthor(
                self.get_argument('signature',None),
                self.get_argument('timestamp',None),
                self.get_argument('nonce',None)
                ,self.get_argument('echostr',None)
                )))

    def post(self):
        bodyString = self.request.body
        print bodyString


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
