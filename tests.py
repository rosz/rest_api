from tornado.testing import AsyncHTTPTestCase
import rest_api
import json


class TestRestApi(AsyncHTTPTestCase):
    # tests for the method adding up numbers
    def get_app(self):
        return rest_api.make_app()

    def test_adding_numbers(self):
        response = self.fetch("/add", body='{"numbers": [1, 2, 3, 4, 5, "abc"]}', method="POST", headers={"Content-Type": "application/json"})
        self.assertEqual(json.loads(response.body.decode('utf8')), {"result": 15})

    def test_adding_numbers_floats(self):
        response = self.fetch("/add", body='{"numbers": [1.2, 2.3, 3.4, "abc"]}', method="POST", headers={"Content-Type": "application/json"})
        self.assertEqual(json.loads(response.body.decode('utf8')), {"result": 6.9})

    def test_adding_numbers_dict_key(self):
        response = self.fetch("/add", body='{"string": [1, 2, 3, 4, 5, "abc"]}', method="POST", headers={"Content-Type": "application/json"})
        self.assertEqual(response.code, 400)

    def test_adding_body_format(self):
        response = self.fetch("/add", body="string", method="POST", headers={"Content-Type": "application/json"})
        self.assertEqual(response.code, 400)

    def test_adding_header_format(self):
        response = self.fetch("/add", body='{"numbers": [1, 2, 3, 4, 5, "abc"]}', method="POST", headers={"string": "string"})
        self.assertEqual(response.code, 400)

    def test_adding_method(self):
        response = self.fetch("/add", body='{"numbers": [1, 2, 3, 4, 5, "abc"]}', method="GET", headers={"Content-Type": "application/json"})
        self.assertEqual(response.code, 599)

    # tests for the method multiplying numbers
    def test_multiplying_numbers(self):
        response = self.fetch("/multiply", body='{"numbers": [1, 2, 3, 4, 5, "abc"]}', method="POST", headers={"Content-Type": "application/json"})
        self.assertEqual(json.loads(response.body.decode('utf8')), {"result": 120})

    def test_multiplying_numbers_floats(self):
        response = self.fetch("/multiply", body='{"numbers": [1.5, 2, 5.5, "abc"]}', method="POST", headers={"Content-Type": "application/json"})
        self.assertEqual(json.loads(response.body.decode('utf8')), {"result": 16.5})

    def test_multiplying_numbers_dict_key(self):
        response = self.fetch("/add", body='{"string": [1, 2, 3, 4, 5, "abc"]}', method="POST", headers={"Content-Type": "application/json"})
        self.assertEqual(response.code, 400)

    def test_multiplying_body_format(self):
        response = self.fetch("/multiply", body="string", method="POST", headers={"Content-Type": "application/json"})
        self.assertEqual(response.code, 400)

    def test_multiplying_header_format(self):
        response = self.fetch("/multiply", body='{"numbers": [1, 2, 3, 4, 5, "abc"]}', method="POST", headers={"string": "string"})
        self.assertEqual(response.code, 400)

    def test_multiplying_method(self):
        response = self.fetch("/multiply", body='{"numbers": [1, 2, 3, 4, 5, "abc"]}', method="GET", headers={"Content-Type": "application/json"})
        self.assertEqual(response.code, 599)

    # tests for the method saving a number
    def test_saving_number(self):
        response = self.fetch("/memory", body='{"number": 10}', method="PUT", headers={"Content-Type": "application/json"})
        self.assertEqual(json.loads(response.body.decode('utf8')), {'status': 'ok'})

    def test_saving_number_float(self):
        response = self.fetch("/memory", body='{"number": 10.5}', method="PUT", headers={"Content-Type": "application/json"})
        self.assertEqual(json.loads(response.body.decode('utf8')), {'status': 'ok'})

    def test_saving_number_more_numbers(self):
        response = self.fetch("/memory", body='{"number": 10, 15}', method="PUT", headers={"Content-Type": "application/json"})
        self.assertEqual(response.code, 400)

    def test_saving_number_dict_key(self):
        response = self.fetch("/add", body='{"string": 10}', method="POST", headers={"Content-Type": "application/json"})
        self.assertEqual(response.code, 400)

    def test_saving_number_format(self):
        response = self.fetch("/memory", body="string", method="PUT", headers={"Content-Type": "application/json"})
        self.assertEqual(response.code, 400)

    def test_saving_number_header_format(self):
        response = self.fetch("/memory", body='{"number": 10}', method="PUT", headers={"string": "string"})
        self.assertEqual(response.code, 400)

    def test_saving_number_method(self):
        response = self.fetch("/memory", body='{"number": 10}', method="GET", headers={"Content-Type": "application/json"})
        self.assertEqual(response.code, 599)

    # tests for method retrieving memory
    def test_getting_memory(self):
        response = self.fetch("/memory", method="GET")
        self.assertEqual(json.loads(response.body.decode('utf8')), {'memory': []})

    def test_getting_memory_method(self):
        response = self.fetch("/memory", method="POST")
        self.assertEqual(response.code, 599)

    # tests for method deleting memory
    def test_deleting_memory(self):
        response = self.fetch("/memory", method="DELETE", headers={"Content-Type": "application/json"})
        self.assertEqual(json.loads(response.body.decode('utf8')), {'status': 'ok'})

    def test_deleting_memory_method(self):
        response = self.fetch("/memory", method="POST")
        self.assertEqual(response.code, 599)
