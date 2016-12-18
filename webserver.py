import tornado.ioloop
import tornado.web
import json

class CheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        print(data)
        self.write({"result":"0"})


def make_app():
    return tornado.web.Application([
        (r"/numberguess", MainHandler),
        (r"/", CheckHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
