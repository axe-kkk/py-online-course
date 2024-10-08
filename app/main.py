from math import ceil


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        print("LOG", cls.days_to_weeks(course_dict["days"]))
        return cls(name=course_dict["name"],
                   description=course_dict["description"],
                   weeks=OnlineCourse.days_to_weeks(course_dict["days"]))

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)
