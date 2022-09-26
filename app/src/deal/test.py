import unittest

from unittest.mock import patch

from database import db_flights
from database import db_users

from deal.contracts import AuthModel
import deal.handler

class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = AuthModel(name="rusteRR", age=19, user_id=1)
        self.db_flights = {
            114: ["25.09.2022 Moscow Saint-Petersburg", 2],
            115: ["25.09.2022 Moscow Sochi", 0],
            116: ["26.09.2022 Sochi Moscow", 3]
        }
        self.db_users = {
        }

    @patch.dict(db_users, {})
    def test_no_more_tickets(self):
        with patch.dict(db_flights, self.db_flights):
            result = deal.handler.check_any_free_tickets(115)
            self.assertEqual(
                result,
                False
            )

    @patch.dict(db_users, {})
    def test_correct_deal(self):
        with patch.dict(db_flights, self.db_flights):
            deal.handler.buy_ticket(114, self.user)
            self.assertEqual(db_users, {
                1: [114],
            })
        
        
    @patch.dict(db_users, {})
    def test_tickets_decrease(self):
        with patch.dict(db_flights, self.db_flights):
            deal.handler.buy_ticket(114, self.user)
            self.assertNotEqual(db_flights[114][1], 0)
            deal.handler.buy_ticket(114, self.user)
            self.assertEqual(db_flights[114][1], 0)
        


if __name__ == '__main__':
    unittest.main()