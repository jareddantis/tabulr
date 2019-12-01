from .course_vwr import CourseViewer

class CourseManager:
    def __init__(self, parent_window):
        self._courses = {}
        self._img_path = ''
        self.parent_window = parent_window
        self.viewer = None
        self.on_viewer_close = None

    def get_courses(self):
        return self._courses.copy()

    @property
    def image_path(self):
        return self._img_path

    @image_path.setter
    def image_path(self, image):
        self._img_path = image

    @property
    def num_courses(self):
        """
        Number of courses added so far.
        """
        return len(self._courses)

    def add_course(self, title, section, venue, instructor):
        self._courses[section] = (title, venue, instructor)

    def check_section(self, section):
        return section in self._courses.keys()

    def set_close_handler(self, fn):
        """
        Sets function to call when the course viewer is closed.
        Currently this is used to update the on-screen course count
        in case the user deletes a course.
        :param fn: Function to call
        """
        self.on_viewer_close = fn

    def view_courses(self):
        """
        Spawn a new window for viewing all entered courses.
        """
        if self.viewer is not None and not self.viewer.closed:
            # Window already spawned
            if not self.viewer.visible:
                # Window is in background, so let's switch to it
                self.viewer.switch_to()
        else:
            # Spawn viewer window
            self.viewer = CourseViewer(self.parent_window, self._courses, self.on_viewer_close)
