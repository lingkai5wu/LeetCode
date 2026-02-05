from collections import deque
from typing import List


class RideSharingSystem:
    rider_q = deque()
    driver_q = deque()
    rider_waiting_set = set()

    def __init__(self):
        self.rider_q.clear()
        self.driver_q.clear()

    def addRider(self, riderId: int) -> None:
        self.rider_q.append(riderId)
        self.rider_waiting_set.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.driver_q.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.rider_q and self.rider_q[0] not in self.rider_waiting_set:
            self.rider_q.popleft()
        if not self.rider_q or not self.driver_q:
            return [-1, -1]
        return [self.driver_q.popleft(), self.rider_q.popleft()]

    def cancelRider(self, riderId: int) -> None:
        self.rider_waiting_set.discard(riderId)
