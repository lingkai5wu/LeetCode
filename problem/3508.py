from bisect import bisect_left, bisect_right
from collections import deque, defaultdict
from typing import List

from util.obj import executeFunctions


class Router:

    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.packet_q = deque()
        self.packet_set = set()
        self.dest_to_timestamps = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False
        if len(self.packet_q) >= self.memory_limit:
            self.forwardPacket()
        self.packet_q.append(packet)
        self.packet_set.add(packet)
        self.dest_to_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packet_q:
            return []
        packet = self.packet_q.popleft()
        self.packet_set.remove(packet)
        self.dest_to_timestamps[packet[1]].popleft()
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dest_to_timestamps[destination]
        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)
        return right - left


if __name__ == '__main__':
    function_names = ["Router", "addPacket", "getCount", "forwardPacket", "getCount", "addPacket", "getCount"]
    parameters_list = [[5], [4, 2, 1], [2, 1, 1], [], [2, 1, 1], [4, 2, 1], [2, 1, 1]]
    print(executeFunctions(Router, function_names, parameters_list))
