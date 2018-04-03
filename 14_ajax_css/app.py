#!/usr/bin/env python
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.escape
import os.path
import json
import datetime
import random

from tornado.options import define, options

define("port", default=3000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        settings = dict(
            debug=True,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages=None)
    
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        now = datetime.datetime.now()
        now = (now.second % 11) * 10
        r = lambda: random.randint(0,255)
        color ="#%02X%02X%02X" %(r(),r(),r())
        response_to_send = dict(now=now, color=color)
        self.write(json.dumps(response_to_send))

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print ("Open http://127.0.0.1:{}".format(options.port))
    main()
