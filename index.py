from tornado import ioloop
from tornado.web import Application, RequestHandler
from json import loads
import os

class fileUploadHandler(RequestHandler):

    def get(self):
        self.write("Upload section")
    
    def post(self):
        data = loads(self.request.body)



class basicRequestHandler(RequestHandler):
    def get(self):
        self.write("Server is working")
   



if __name__ == "__main__":

    app = Application([
        (r"/", basicRequestHandler),
        (r"/upload", fileUploadHandler)
    ])

    print "Now listening on port 8080"
    PORT = int(os.environ.get("PORT", 8080))
    app.listen(PORT)
    ioloop.IOLoop.current().start()