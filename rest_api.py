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
        numbers = self.request.body
        # numbers = numbers.decode('utf-8')
        numbers_array = json.loads(numbers)
        result = 0
        for number in numbers_array:
            number = int(number)
            result += number
        self.write(result)
    get = post

# multiply numbers from memory
class MultiplyNumbers(RequestHandler):
    def post(self):
        numbers = self.request.body
        numbers = numbers.decode('utf-8')
        numbers_array = json.loads(numbers)
        result = 1
        for number in numbers_array:
            number = int(number)
            result *= number
        self.write(result)
    get = post

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
        (r"/memory", SaveNumbers)
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
