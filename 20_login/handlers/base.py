#-*- coding:utf-8 -*-

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        print ("BaseHandler get_current_user")
        data = self.get_secure_cookie("user")
        # print  ("user == ",self.current_user)
        print ("data == ",data)
        return data

class LoginHandler(BaseHandler):
    def get(self):
        print ("LoginHandler get")
        incorrect = self.get_secure_cookie("incorrect")
        if incorrect and int(incorrect) > 25 :
            self.write('<center>blocked</center>')
            return
        self.render('login.html')

    def post(self):
        print ("LoginHandler post")
        getusername = self.get_argument('username')
        getpassword = self.get_argument('password')
        if "demo" == getusername and "demo" == getpassword : 
            print ("upper")
            self.set_secure_cookie("usder", self.get_argument("username"))
            self.set_secure_cookie("incorrect", "0")
            self.redirect(self.reverse_url("main"))
        else:
            incorrect = self.get_secure_cookie("incorrect")
            print ("incorrect == ",incorrect)
            if not incorrect:
                incorrect = 0
            self.set_secure_cookie("incorrect", str(int(incorrect)+1))
            self.write('<center>something wrong with your data <a href="/">Go Home</a></center>')

class LogoutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        print ("logout")
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", self.reverse_url("main")))