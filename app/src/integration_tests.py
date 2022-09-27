from http import client
import unittest

from fastapi import FastAPI

from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app
from database import db_flights
from database import db_users
from database import db_users_data
from schedule.routers import router as schedule_router
from auth.routers import router as auth_router
from deal.routers import router as deal_router


class TestStringMethods(unittest.TestCase):
    client = TestClient(app)

    def setUp(self) -> None:
        super().setUp()
        app = FastAPI()
        self.db_flights = {
            114: ["25.09.2022 Moscow Saint-Petersburg", 2],
            115: ["25.09.2022 Moscow Sochi", 0],
            116: ["26.09.2022 Sochi Moscow", 3],
        }
        self.db_users_data = {"rusteRR": ["123", "Alex"]}

    def test_get_schedule(self):
        with patch.dict(db_flights, self.db_flights):
            response = self.client.get(
                "/schedule/planes/date/25.09.2022/city/Moscow/Saint-Petersburg"
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {"Possible options": {"1": "25.09.2022 Moscow Saint-Petersburg"}},
            )

    @patch.dict(db_users, {})
    def test_make_deal(self):
        with patch.dict(db_flights, self.db_flights):
            response = self.client.post(
                "/deal/114", json={"name": "Alex", "age": 19, "login": "rusteRR"}
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {"OK": "You bought tickets on flight 114"},
            )

    def test_auth(self):
        with patch.dict(db_users_data, self.db_users_data):
            response = self.client.post(
                "/auth/register",
                json={"name": "Alex", "password": "1234", "login": "rusteRR"},
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {"Error": "User is already registered"},
            )
            response = self.client.post(
                "/auth/register",
                json={"name": "Bred", "password": "12345", "login": "Bred123"},
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json(),
                {"OK": "User Bred123 has been succesfully registered"},
            )


if __name__ == "__main__":
    unittest.main()
