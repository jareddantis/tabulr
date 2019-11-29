from scenes.b2_course_view import CourseViewer

class CourseManager:
    def __init__(self, bus):
        self.courses = {}
        self.viewer = None
        self.bus = bus

    @property
    def num_courses(self):
        return len(self.courses)

    def add_course(self, title, venue, instructor):
        self.courses[title] = (venue, instructor)

    def view_courses(self):
        self.viewer = CourseViewer(self.bus, self.courses)
