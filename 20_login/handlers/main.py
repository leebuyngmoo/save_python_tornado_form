import tornado.web
import utils.cipher
from .base import BaseHandler

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        print ("MainHandler get")
        self.render("main.html", nonce = utils.cipher.get_nonce())

