from tornado import ioloop
from tornado.web import Application, RequestHandler
from json import loads
import os
import base64

class fileUploadHandler(RequestHandler):

    def get(self):
        self.write("Upload section")
    
    def post(self):
        files = self.request.files
        #file_ = self.request.files["fileFromNetSuite"][0]
        #fileName = file_["filename"]
        self.write(str(files)+" was selected")



class basicRequestHandler(RequestHandler):
    def get(self):
        self.write("Server is working")
   



if __name__ == "__main__":

    app = Application([
        (r"/", basicRequestHandler),
        (r"/upload", fileUploadHandler)
    ])

    print("Now listening on port 8080")
    PORT = int(os.environ.get("PORT", 8080))
    app.listen(PORT)
    ioloop.IOLoop.current().start()