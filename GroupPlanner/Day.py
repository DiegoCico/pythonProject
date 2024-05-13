from typing import List

class Day:
    def __init__(self, day: int):
        self.day = day
        self.schedule = []

    def get_day(self) -> int:
        return self.day

    def edit_schedule(self, schedule: List[str]):
        self.schedule = schedule

    def get_schedule(self) -> List[str]:
        return self.schedule

    def add_activity(self, activity):
        self.schedule.append(activity)
