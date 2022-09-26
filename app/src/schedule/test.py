import unittest

from unittest.mock import patch

from database import db_flights

import schedule.handler

class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.db_flights = {
            114: ["25.09.2022 Moscow Saint-Petersburg", 4],
            115: ["25.09.2022 Moscow Sochi", 2],
            116: ["26.09.2022 Sochi Moscow", 3]
        }

    def test_correct_query(self):
        with patch.dict(db_flights, self.db_flights):
            result = schedule.handler("25.09.2022", "Moscow", "Saint-Petersburg")
            self.assertEqual(
                result,
                {"Possible options": {"1": "25.09.2022 Moscow Saint-Petersburg"}},
            )

    def test_no_flights_av(self):
        with patch.dict(db_flights, self.db_flights):
            result = schedule.handler(
                "27.09.2022", "Moscow", "Saint-Petersburg"
            )
            self.assertEqual(
                result,
                {"Possible options": {}},
            )

    def test_correct_order(self):
        with patch.dict(db_flights, self.db_flights):
            result = schedule.handler(
                "27.09.2022", "Saint-Petersburg", "Moscow"
            )
            self.assertEqual(
                result,
                {"Possible options": {}},
            )

if __name__ == '__main__':
    unittest.main()