from deal.contracts import AuthModel

from database import db_flights
from database import db_users


def check_any_free_tickets(flight_id: int):
    return db_flights[int(flight_id)][1] > 0


def buy_ticket(flight_id: int, user: AuthModel):
    if not check_any_free_tickets(flight_id):
        return {"Error": "No more tickets to buy"}
    db_flights[int(flight_id)][1] -= 1
    db_users[user.login] = db_users.get(user.login, []) + [flight_id]
    return {"OK": "You bought tickets on flight " + str(flight_id)}
