class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        prev_time = 0
        fleet = 0

        for pos, speed in cars:
            time_to_arrive = (target - pos) / speed

            if time_to_arrive > prev_time:
                fleet += 1
                prev_time = time_to_arrive
        
        return fleet