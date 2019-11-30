from scenes.b2_course_view import CourseViewer

class CourseManager:
    def __init__(self, parent_window, bus):
        self.courses = {}
        self.parent_window = parent_window
        self.viewer = None
        self.bus = bus

    @property
    def num_courses(self):
        return len(self.courses)

    def add_course(self, title, section, venue, instructor):
        self.courses[title] = (section, venue, instructor)

    def view_courses(self):
        if self.viewer is not None and not self.viewer.closed:
            # Window already spawned
            if not self.viewer.is_viewing:
                # Window is in background, so let's switch to it
                self.viewer.switch_to()
        else:
            # Spawn viewer window
            self.viewer = CourseViewer(self.parent_window, self.bus, self.courses)
            self.viewer.switch_to()
