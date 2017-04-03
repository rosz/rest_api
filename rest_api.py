import tornado.ioloop
import json
from tornado.web import RequestHandler

# MainHandler
class MainHandler(RequestHandler):
    def get(self):
        self.write("REST API based on Tornado framework")


# sum up numbers from memory
class SumUpNumbers(RequestHandler):
    def post(self):
        self.write("adding numbers")


# multiply numbers from memory
class MultiplyNumbers(RequestHandler):
    def post(self):
        self.write("multiplying numbers")


# save new number in memory
class SaveNumbers(RequestHandler):
    def put(self):
        self.write("saving numbers in the memory")

    def get(self):
        self.write("printing out numbers from the memory")

    def delete(self):
        self.write("delete numbers from the memory")


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/add", SumUpNumbers),
        (r"/multiply", MultiplyNumbers),
        (r"/memory", SaveNumbers),
        (r"/memory", SaveNumbers),
        (r"/memory", SaveNumbers)
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
