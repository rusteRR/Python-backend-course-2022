import sys

import grpc
from requests import request

from protobuf.builds.GreetingService_pb2 import Flight, Null
from protobuf.builds.GreetingService_pb2_grpc import FlightServiceStub


def get_flight(port: int, date1: str, city_from1: str, city_to1: str) -> bool:
    """_summary_

    Args:
        port (int): port to connect server
        date (str): date of flight
        city_from (str): city to start flight
        city_to (str): city to end flight
    """
    with grpc.insecure_channel("localhost:3000") as channel:
        client = FlightServiceStub(channel)

        confirmation = client.getFlight(request=Flight(
            date=date1,
            city_from=city_from1,
            city_to=city_to1
        ))
    
        return confirmation.is_flight_available