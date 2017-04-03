import tornado.ioloop
import tornado.web
import json


# MainHandler
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("REST API based on Tornado framework")


# sum up numbers from the memory
class SumUpNumbers(tornado.web.RequestHandler):
    def get(self):
        self.write("adding numbers")


# multiply numbers from the memory
class MultiplyNumbers(tornado.web.RequestHandler):
    def get(self):
        self.write("multiplying numbers")


# save new number in the memory
class SaveNumbers(tornado.web.RequestHandler):
    def get(self):
        self.write("saving numbers in the memory")


# return all the numbers from the memory
class ReturnNumbers(tornado.web.RequestHandler):
    def get(self):
        self.write("printing out numbers from the memory")


# clean up memory
class DeleteNumbers(tornado.web.RequestHandler):
    def get(self):
        self.write("delete numbers from the memory")


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/add", SumUpNumbers),
        (r"/multiply", MultiplyNumbers),
        (r"/put-memory", SaveNumbers),
        (r"/get-memory", ReturnNumbers),
        (r"/delete", DeleteNumbers)
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
