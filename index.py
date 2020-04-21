from tornado import ioloop
from tornado.web import Application, RequestHandler
from json import loads, dumps
import os
import base64

class fileUploadHandler(RequestHandler):

    def get(self):
        self.write("Upload section")
    
    def post(self):
        files = self.request.files

        fileObj = files.get("fileFromNetSuite", [])[0]
        self.write(dumps({"url": "https://somefakeurl.com"}))
        #response = self.processFile(fileObj)
        #self.replyToClient(response)        
        

    def replyToClient(self, dataToBeSentToClient):
        """Sends data back to client in the form of JSON"""
        data = dumps(dataToBeSentToClient)
        self.write(data)

    def processFile(self, fileObj):
        """Processes file and returns details to send to client"""
        filename = fileObj.get("filename")
        fileBody = fileObj.get("body")
        fileType = fileObj.get("content_type")


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