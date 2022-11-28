"""This file serves as our testing library for app.py"""
import json
import flask_unittest
from app import create_app

class TestParse(flask_unittest.ClientTestCase):
    """Tests for winter and fall course searches"""
    app = create_app()

    def test_return_static(self, client):
        """tests that the html exists"""
        res = client.get('/')
        self.assertIsNotNone(res)
        self.assertTrue('<!doctype html>' in res.data.decode("utf-8"))

    def test_get_selector_data_fall(self, client):
        """tests that there are the correct number of fall courses"""
        res = client.post('/allCourseSections', json={ 'selectedTerm': 'Fall' })
        print(res.data)
        data = json.loads(res.data)
        self.assertEqual(3036, len(data))

    def test_get_selector_data_winter(self, client):
        """tests that there are the correct number of winter courses"""
        res = client.post('/allCourseSections', json={ 'selectedTerm': 'Winter' })
        print(res.data)
        data = json.loads(res.data)
        self.assertEqual(2792, len(data))

    def test_get_courses_fall(self, client):
        """tests 2 courses from the fall"""

        mock_req = { "courses": [
                        {
                            "value": "ACCT1220",
                            "label": "ACCT*1220*0105 (6577) Intro Financial Accounting"
                        },
                        {
                            "value": "ACCT3330",
                            "label": "ACCT*3330*02 (6589) Intermed Financial Account I"
                        }],
                        "selectedTerm": "Fall"
                    }
        # pylint: disable=line-too-long
        expected_json = [{'Academic Level': 'Undergraduate', 'Available': '1 / 48', 'Credits': '0.50', 'Faculty': 'P. Lassou', 'Location': 'Guelph', 'Meeting Information': {'exam': [['Tues'], ['08:30AM', '10:30AM', '(2022/12/06)'], 'Room TBA', '\n'], 'lec': [['Fri'], ['08:30AM', '10:20AM'], 'ROZH', 'Room 104'], 'seminar': [['Mon'], ['11:30AM', '12:20PM'], 'MCKN', 'Room 226']}, 'Name': 'ACCT*1220*0105 (6577) Intro Financial Accounting', 'Status': 'Open', 'Term': 'Fall 2022'}, {'Academic Level': 'Undergraduate', 'Available': '8 / 76', 'Credits': '0.50', 'Faculty': 'S. Wick', 'Location': 'Guelph', 'Meeting Information': {'exam': [['Mon'], ['02:30PM', '04:30PM', '(2022/12/12)'], 'Room TBA', '\n'], 'lec': [['Mon', 'Wed'], ['01:00PM', '02:20PM'], 'MCKN', 'Room 121']}, 'Name': 'ACCT*3330*02 (6589) Intermed Financial Account I', 'Status': 'Open', 'Term': 'Fall 2022'}]

        res = client.post('/courses', json=mock_req)
        response_json = json.loads(res.data)
        self.assertEqual(response_json, expected_json)

    def test_get_courses_winter(self, client):
        """tests 2 courses from the winter"""
        mock_req = { "courses": [
                        {
                            "value": "ACCT1220",
                            "label": "ACCT*1220*0101 (1065) Intro Financial Accounting"
                        },
                        {
                            "value": "ACCT1220",
                            "label": "ACCT*1220*0102 (1066) Intro Financial Accounting"
                        }],
                        "selectedTerm": "Winter"
                    }
        # pylint: disable=line-too-long
        expected_json = [{'Meeting Information': {'lec': [['Fri'], ['08:30AM', '10:20AM'], 'ROZH', 'Room 104'], 'seminar': [['Tues'], ['10:30AM', '11:20AM'], 'MCKN', 'Room 230']}, 'Term': 'Winter 2023', 'Status': 'Open', 'Name': 'ACCT*1220*0101 (1065) Intro Financial Accounting', 'Location': 'Guelph', 'Faculty': 'S. Dhaliwal', 'Available': '25 / 25', 'Credits': '0.50', 'Academic Level': 'Undergraduate'}, {'Meeting Information': {'lec': [['Fri'], ['08:30AM', '10:20AM'], 'ROZH', 'Room 104'], 'seminar': [['Mon'], ['02:30PM', '03:20PM'], 'MCKN', 'Room 231']}, 'Term': 'Winter 2023', 'Status': 'Open', 'Name': 'ACCT*1220*0102 (1066) Intro Financial Accounting', 'Location': 'Guelph', 'Faculty': 'S. Dhaliwal', 'Available': '25 / 25', 'Credits': '0.50', 'Academic Level': 'Undergraduate'}]
        res = client.post('/courses', json=mock_req)
        response_json = json.loads(res.data)
        self.assertEqual(response_json, expected_json)

    def test_get_courses_empty_fall(self, client):
        """tests a empty search for fall"""
        mock_req = { "courses": [], "selectedTerm": "Fall" }
        res = client.post('/courses', json=mock_req)
        response_json = json.loads(res.data)
        self.assertEqual(response_json, [])

    def test_get_courses_empty_winter(self, client):
        """tests a empty search for winter"""

        mock_req = { "courses": [], "selectedTerm": "Winter" }
        res = client.post('/courses', json=mock_req)
        response_json = json.loads(res.data)
        self.assertEqual(response_json, [])
