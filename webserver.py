import os
import tornado.web
import tornado.httpserver
import tornado.ioloop


print('start Webserver')
SERVER_PORT = 9090

currenPath = os.path.dirname(os.path.abspath(__file__))
resourcesPath = currenPath + '/static'

class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class webApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexPageHandler),
            (r'/(.*)', tornado.web.StaticFileHandler, {'path': resourcesPath})
        ]

        settings = {
            'static_path': resourcesPath,
            'template_path': 'static'
        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    ws_app = webApplication()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(SERVER_PORT);
    print('Listening on ',SERVER_PORT)
    tornado.ioloop.IOLoop.instance().start()