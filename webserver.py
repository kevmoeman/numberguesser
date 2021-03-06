import tornado.ioloop
import tornado.web
import json
import display_numbers

clf = None
class CheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        print(self.request.body)
        data = tornado.escape.json_decode(self.request.body)
        val = clf.predict(data)
        print(val)
        rtv = {"result":int(val[0])}
        print(rtv)
        self.write(tornado.escape.json_encode(rtv))

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        self.set_status(204)
        self.finish()


def make_app():
    return tornado.web.Application([
        (r"/numberguess", MainHandler),
        (r"/", CheckHandler)
    ])

if __name__ == "__main__":
    #train the model
    clf = display_numbers.train_model()
    #start the server
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
