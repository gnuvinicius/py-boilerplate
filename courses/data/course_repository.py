from config import session
from ..models.course_models import Course


class CourseRepository:

    async def create_course(self, course: Course):
        async with session() as s:
            s.add(course)
            await s.commit()
