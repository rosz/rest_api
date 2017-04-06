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
        # decoding JSON
        numbers = self.request.body
        numbers = numbers.decode('utf-8')
        numbers_array = json.loads(numbers)
        result = 0

        # arithmetics, add up numbers
        for number in numbers_array["numbers"]:
            number = int(number)
            result += number

        result_dict = {"result": result}

        # encoding JSON
        return json.dumps(result_dict)

# multiply numbers from memory
class MultiplyNumbers(RequestHandler):
    def post(self):
        # decoding JSON
        numbers = self.request.body
        numbers = numbers.decode('utf-8')
        numbers_array = json.loads(numbers)
        result = 1

        # arithmetics, add up numbers
        for number in numbers_array["numbers"]:
            number = int(number)
            result += number

        result_dict = {"result": result}

        # encoding JSON
        return json.dumps(result_dict)

# memory as list
saved_numbers = []


# manipulate memory
class SaveNumbers(RequestHandler):
    # save new number in memory, return status
    def put(self):
        number = self.request.body
        number = number.decode('utf-8')
        number_dict = json.loads(number)
        saved_numbers.append(number_dict["number"])
        json.dumps(saved_numbers)

        status = {"status" : "ok"}
        return json.dumps(status)

    # return all numbers from memory
    def get(self):
        result_dict = {"memory": saved_numbers}
        return json.dumps(result_dict)

    # clean memory, return status
    def delete(self):
        saved_numbers = []
        status = {"status" : "ok"}
        return json.dumps(status)


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/add", SumUpNumbers),
        (r"/multiply", MultiplyNumbers),
        (r"/memory", SaveNumbers)
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
