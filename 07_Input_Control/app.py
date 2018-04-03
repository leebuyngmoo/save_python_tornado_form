#-*- coding:utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
import os.path
import logging

from tornado.options import define, options

define("port", default=3000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        settings = {
            "template_path":os.path.join(base_dir, "templates"),
            "static_path":os.path.join(base_dir, "static"),
            "debug":True,
        }
        tornado.web.Application.__init__(self, [
        tornado.web.url("r/(favicon.ico)", tornado.web.StaticFileHandler, {"path":""}),
        tornado.web.url("/", MainHandler, name="main"),
        ], **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        userinfo = None 
        self.render("index.html", userinfo=userinfo)

    def post(self):
        userinfo = dict( nickname = self.get_argument('nickname'),
                         frequency = self.get_argument('frequency') )
        #self.write("{}{}".format(nickname, frequency))
        self.render("index.html", userinfo=userinfo)


def main():
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    logging.warning("http://127.0.0.1:{}".format(options.port))
    main()

