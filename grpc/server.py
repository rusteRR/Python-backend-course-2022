from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

import grpc

from database import db_flights

from protobuf.builds.GreetingService_pb2 import Confirmation
from protobuf.builds.GreetingService_pb2_grpc import FlightServiceServicer, add_FlightServiceServicer_to_server


class Service(FlightServiceServicer):
    def IsFlightAvailable(self, date: str, city_from: str, city_to: str) -> bool:
        """Database access to check if flight is available

        Args:
            date (str): date of flight
            city_from (str): city to start
            city_to (str): city to end

        Returns:
            bool: return true if flight is found in database
        """        
        return " ".join([date, city_from, city_to]) in db_flights.values()

    def getFlight(self, request, context):
        return Confirmation(is_flight_available=self.IsFlightAvailable(request.date, request.city_from, request.city_to))

def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_FlightServiceServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()