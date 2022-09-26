import unittest

from unittest.mock import patch

from database import db_users_data

from auth.contracts import AuthModel
import auth.handler


class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.db_users_data = {"rusteRR": ["123", "Alex"]}
        self.user = AuthModel(login="Bred123", password="qwerty", name="Bred")

    def test_already_registered(self):
        with patch.dict(db_users_data, self.db_users_data):
            result = auth.handler.register(AuthModel(login="rusteRR", password="12345", name="Alex"))
            self.assertEqual(result, {"Error": "User is already registered"})

    def test_correct_register(self):
        with patch.dict(db_users_data, self.db_users_data):
            result = auth.handler.register(self.user)
            self.assertEqual(
                result, {"OK": "User Bred123 has been succesfully registered"}
            )

    def test_register_twice(self):
        with patch.dict(db_users_data, self.db_users_data):
            result = auth.handler.register(self.user)
            self.assertEqual(
                result, {"OK": "User Bred123 has been succesfully registered"}
            )
            result = auth.handler.register(self.user)
            self.assertEqual(result, {"Error": "User is already registered"})


if __name__ == "__main__":
    unittest.main()
