from random import shuffle
from typing import List, Optional
import xlsxwriter
from GroupPlanner.Day import Day


class Processor:
    def __init__(self, total_periods: int, lunch_period: int, duration_of_day: float, activities: List[str], group: int):
        self.total_periods = total_periods
        self.lunch_period = lunch_period
        self.duration_of_day = duration_of_day
        if group >= len(activities):
            self.activities = activities
            self.group = group
        else:
            print(f"Too many activities, not enough groups, shortening the amount of groups to {len(activities)}")
            self.activities = activities
            self.group = len(activities)
        self.week = List[Day]

    def activity_length(self) -> float:
        return round(self.total_periods / self.duration_of_day, 1)

    def sort_week(self):
        self.week.sort(key=lambda day: day.get_day())

    def sorting_activities_day(self, date: int):
        day = [Day(date) for _ in range(self.group)]
        remaining_activities = self.activities[:]
        shuffle(remaining_activities)

        for p in range(self.total_periods):
            if p == self.lunch_period:
                for d in day:
                    d.add_activity("LUNCH")
                continue

            if not remaining_activities:
                remaining_activities = self.activities[:]
                shuffle(remaining_activities)

            activity = remaining_activities.pop(0)
            for d in day:
                d.add_activity(activity)

        self.week.extend(day)
        self.sort_week()

    def create_table(self):
        workbook = xlsxwriter.Workbook('GroupPlanner.xlsx')
        worksheet = workbook.add_worksheet()
        self.format_table(worksheet)
        for i in range(5):
            self.sorting_activities_day(i)

        row = 1
        col = 1
        for day in self.week:
            row = 1
            for activity in day.get_schedule():
                worksheet.write(row, col, activity)
                row += 1
            col += 1

        workbook.close()

    def format_table(self, worksheet):
        col = 0
        row = 0
        content = ["", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
        bold = worksheet.book.add_format({'bold': True})
        for item in content:
            worksheet.write(row, col, item, bold)
            col += 1
        for group in range(self.group):
            worksheet.write(row + 1, group + 1, "Duration " + str(self.activity_length()))



    def is_cross_over(self) -> Optional[List[Day]]:
        for d in range(0, 5):
            for i in range(len(self.week)):
                checking = self.week[i]
                for j in range(i + 1, len(self.week)):
                    current = self.week[j]
                    if checking.get_day() != current.get_day():
                        break
                    activities_checking = checking.get_schedule()
                    activities_current = current.get_schedule()

                    for idx, activity in enumerate(activities_checking):
                        if idx < len(activities_current) and activity == activities_current[idx]:
                            return [checking, current]
        return None









