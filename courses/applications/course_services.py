from courses.data.course_repository import CourseRepository
from ..models.course_models import Course
from asyncio import run


class CourseService:

    def __init__(self) -> None:
        self.repository = CourseRepository()

    def create_course(self, course: Course):
        run(self.repository.create_course(course))
