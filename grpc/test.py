import unittest

from parameterized import parameterized

from unittest.mock import patch

from client import get_flight

from database import db_flights


class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.db_flights = {
            114: "25.09.2022 Moscow Saint-Petersburg",
            115: "25.09.2022 Moscow Sochi",
            116: "26.09.2022 Sochi Moscow",
        }

    @parameterized.expand(
        [
            ["flight_avaiable", 3000, "25.09.2022", "Moscow", "Sochi", True],
            ["flight_unavaiable", 3000, "26.09.2022", "Moscow", "Sochi", False],
        ]
    )
    def test_get_schedule(
        self, name: str, port: int, date: str, city_from: str, city_to: str, result: bool
    ):
        """Test functional

        Args:
            port (int): _description_
            date (str): _description_
            city_from (str): _description_
            city_to (str): _description_
            result (bool): expected result of request
        """
        with patch.dict(db_flights, self.db_flights):
            self.assertEqual(get_flight(port, date, city_from, city_to), result)
            


if __name__ == "__main__":
    unittest.main()
