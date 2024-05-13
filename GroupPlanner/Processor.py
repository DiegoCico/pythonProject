from random import shuffle
from typing import List, Optional
import xlsxwriter
from GroupPlanner.Day import Day


class Processor:
    def __init__(self, total_periods: int, lunch_period: int, duration_of_day: float, activities: List[str], group: int):
        self.total_periods = total_periods
        self.lunch_period = lunch_period
        self.duration_of_day = duration_of_day
        if len(activities) >= group:
            self.activities = activities
            self.group = group
        else:
            print(f"Too many groups, not enough activity, shortening the amount of groups to {len(activities)}")
            self.activities = activities
            self.group = len(activities)
        self.week: List[Day] = []

    def activity_length(self) -> float:
        return round(self.total_periods / self.duration_of_day, 1)

    def sort_week(self):
        self.week.sort(key=lambda day: day.get_day())

    def sorting_activities_day(self, date: int):
        day = [Day(date) for _ in range(self.group)]
        remaining_activities = self.activities[:]

        for g in range(self.group):
            group_activities = remaining_activities[g:] + remaining_activities[:g]
            for p in range(self.total_periods):
                if p == self.lunch_period:
                    day[g].add_activity("LUNCH")
                    continue
                shuffle(group_activities)

                if not group_activities:
                    group_activities = remaining_activities[g:] + remaining_activities[:g]

                activity = group_activities.pop(0)
                day[g].add_activity(activity)

        self.week.extend(day)
        self.sort_week()

    def create_table(self):
        workbook = xlsxwriter.Workbook('GroupPlanner.xlsx')
        worksheet = workbook.add_worksheet()
        start_row = 0

        for i in range(5):
            self.sorting_activities_day(i)

        for g in range(self.group):
            self.format_table(workbook, worksheet, start_row, g)
            col = 1
            for i in range(g, len(self.week), self.group):
                row = start_row + 1
                day = self.week[i]
                for activity in day.get_schedule():
                    worksheet.write(row, col, activity)
                    row += 1
                col += 1
            start_row += self.total_periods + 3

        workbook.close()

    def format_table(self, workbook, worksheet, start_row, group_index):
        col = 0
        row = start_row
        content = ["", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
        cell_format = workbook.add_format()
        cell_format.set_bold(True)
        for item in content:
            worksheet.write(row, col, item, cell_format)
            col += 1
        worksheet.write(row + 1, 0, f"Group {group_index + 1}", cell_format)
        worksheet.write(row + 1, 1, "Duration " + str(self.activity_length()))

    def is_cross_over(self) -> Optional[List[Day]]:
        for i in range(len(self.week)):
            checking = self.week[i]
            for j in range(i + 1, len(self.week)):
                current = self.week[j]
                if checking.get_day() != current.get_day():
                    continue
                activities_checking = checking.get_schedule()
                activities_current = current.get_schedule()

                for idx, activity in enumerate(activities_checking):
                    if idx < len(activities_current) and activity == activities_current[idx]:
                        return [checking, current]
        return None
