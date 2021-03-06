import tornado.ioloop
import json
import functools
from tornado.web import RequestHandler
from tornado.web import HTTPError
from numbers import Number

class BasicHandler(RequestHandler):
    # verify if Content-Type == application/json
    def verify_json(self, header):
        if header.get("Content-Type", "") != "application/json":
            raise HTTPError(400, "wrong format, JSON expected")

    # unify input json data to proceed
    def unify_data(self, body):
        numbers = body.decode('utf-8')
        try:
            numbers_dict = json.loads(numbers)
        except:
            raise HTTPError(400, "wrong format, JSON expected")
        return numbers_dict

# sum up numbers from memory
class SumUpNumbers(BasicHandler):
    def post(self):
        # catch format exceptions
        self.verify_json(self.request.headers)
        # decoding JSON
        data = self.unify_data(self.request.body)
        # catch exception: key value error
        if "numbers" not in data:
            raise HTTPError(400, "dictionary key not found")

        # arithmetics, add up numbers
        numbers_list = data["numbers"]
        result = sum(filter(lambda n: isinstance(n, Number), numbers_list))
        if result == int(result):
            result = int(result)

        result_dict = {"result": result}

        # encoding JSON
        self.write(result_dict)

# multiply numbers from memory
class MultiplyNumbers(BasicHandler):
    def post(self):
        # catch format exceptions
        self.verify_json(self.request.headers)
        # decoding JSON
        data = self.unify_data(self.request.body)
        # catch exception: key value error
        if "numbers" not in data:
            raise HTTPError(400, "dictionary key not found")

        # arithmetics, multiply numbers
        numbers_list = data["numbers"]
        result = functools.reduce(lambda x, y: x * y, filter(lambda n: isinstance(n, Number), numbers_list))
        if result == int(result):
            result = int(result)
        result_dict = {"result": result}

        # encoding JSON
        self.write(result_dict)

# memory as list
saved_numbers = []


# manipulate memory
class SaveNumbers(BasicHandler):
    # save new number in memory, return status
    def put(self):
        # catch format exceptions
        self.verify_json(self.request.headers)
        # decoding JSON
        data = self.unify_data(self.request.body)
        # catch exception: key value error
        if "number" not in data:
            raise HTTPError(400, "dictionary key not found")

        # catch data type exception
        if not isinstance(data["number"], Number):
            raise HTTPError(400, "only numeral format expected")

        saved_numbers.append(data["number"])
        status = {"status": "ok"}
        self.write(status)

    # return all numbers from memory
    def get(self):
        result_dict = {"memory": saved_numbers}
        self.write(result_dict)

    # clean memory, return status
    def delete(self):
        global saved_numbers
        saved_numbers = []
        status = {"status": "ok"}
        self.write(status)


def make_app():
    return tornado.web.Application([
        (r"/", SumUpNumbers),
        (r"/add", SumUpNumbers),
        (r"/multiply", MultiplyNumbers),
        (r"/memory", SaveNumbers)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
