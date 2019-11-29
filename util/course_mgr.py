class CourseManager:
    def __init__(self):
        self.courses = {}

    @property
    def num_courses(self):
        return len(self.courses)

    def add_course(self, title, venue, instructor):
        self.courses[title] = (venue, instructor)
