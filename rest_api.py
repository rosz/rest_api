import tornado.ioloop
import json
from tornado.web import RequestHandler
from tornado.web import HTTPError
from numbers import Number

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
        try:
            numbers_dict = json.loads(numbers)
        except:
            raise HTTPError(400, "wrong format, JSON expected")

        if "numbers" not in numbers_dict:
            raise HTTPError(400, "dictionary key not found")

        # arithmetics, add up numbers
        result = 0
        for number in numbers_dict["numbers"]:
            try:
                number = float(number)
            except ValueError:
                raise HTTPError(400, "only numeral format expected")
            result += number

        if result == int(result):
            result = int(result)

        result_dict = {"result": result}

        # encoding JSON
        return self.write(json.dumps(result_dict))

# multiply numbers from memoryczy wystarczy, że zrobię
class MultiplyNumbers(RequestHandler):
    def post(self):
        # decoding JSON
        numbers = self.request.body
        numbers = numbers.decode('utf-8')
        try:
            numbers_dict = json.loads(numbers)
        except:
            raise HTTPError(400, "wrong format, JSON expected")

        if "numbers" not in numbers_dict:
            raise HTTPError(400, "dictionary key not found")

        # arithmetics, add up numbers
        result = 1
        for number in numbers_dict["numbers"]:
            try:
                number = float(number)
            except ValueError:
                raise HTTPError(400, "only numeral format expected")
            result *= number

        if result == int(result):
            result = int(result)

        result_dict = {"result": result}

        # encoding JSON
        return self.write(json.dumps(result_dict))

# memory as list
saved_numbers = []


# manipulate memory
class SaveNumbers(RequestHandler):
    # save new number in memory, return status
    def put(self):
        number = self.request.body
        number = number.decode('utf-8')
        try:
            number_dict = json.loads(number)
        except:
            raise HTTPError(400, "wrong format, JSON expected")

        if "number" not in number_dict:
            raise HTTPError(400, "dictionary key not found")

        if not isinstance(number_dict["number"], Number):
            raise HTTPError(400, "only numeral format expected")

        saved_numbers.append(number_dict["number"])
        json.dumps(saved_numbers)

        status = {"status": "ok"}
        return self.write(json.dumps(status))

    # return all numbers from memory
    def get(self):
        result_dict = {"memory": saved_numbers}
        return self.write(json.dumps(result_dict))

    # clean memory, return status
    def delete(self):
        global saved_numbers
        saved_numbers = []
        status = {"status": "ok"}
        return self.write(json.dumps(status))


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/add", SumUpNumbers),
        (r"/multiply", MultiplyNumbers),
        (r"/memory", SaveNumbers)
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
