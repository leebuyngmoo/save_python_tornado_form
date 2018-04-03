#-*- coding:utf-8 -*-
import tornado.web
import motor
import logging

from .base import BaseHandler
from utils.cipher import *
from tornado import gen

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html")
    
    @gen.coroutine
    def post(self):
        db = motor.MotorClient('localhost').testdb
        getusername = self.get_argument('username')
        getpassword = self.get_argument('password')
        check = yield db.userinfo.find_one(dict(username=getusername))
        logging.warning(check)
        if check == None : 
            hashed_pw = get_hash(getpassword)
            insert_check = yield db.userinfo.insert(dict(username=getusername,
                                                        password=hashed_pw))
            self.redirect("/")
        else : self.redirect("/register")
                   
