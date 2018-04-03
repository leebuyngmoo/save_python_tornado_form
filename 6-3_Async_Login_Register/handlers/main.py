#-*- coding:utf-8 -*-
import tornado.web
import tornado.gen
from .base import BaseHandler

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    @tornado.gen.coroutine
    def get(self):
        user = self.get_secure_cookie('user')
        self.render("main.html",user=user)
