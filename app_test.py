from app import app

import unittest
import json

class StunticonTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_stunticons(self):
        response = self.tester.get(
            '/stunticons.json', content_type='application/json'
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(
            json.dumps([
                "Motormaster",
                "Dead End",
                "Breakdown",
                "Wildrider",
                "Drag Strip"
            ]),
            response.data,
        )

if __name__ == '__main__':
    unittest.main()
