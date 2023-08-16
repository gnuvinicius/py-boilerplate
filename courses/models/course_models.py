from typing import List, Optional
from uuid import uuid4
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

Base = declarative_base()


class Course(Base):
    __tablename__ = 'tb_course'

    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30), unique=True)
    description: Mapped[Optional[str]]
    students: Mapped[List['Student']] = relationship(
        back_populates='course', cascade='all, delete-orphan')

    def __init__(self, title, description):
        self.id = str(uuid4())
        self.title = title
        self.description = description

    def __repr__(self):
        return f'Course({self.title})'


class Student(Base):
    __tablename__ = 'tb_student'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    course_id: Mapped[str] = mapped_column(ForeignKey("tb_course.id"))
    course: Mapped['Course'] = relationship(back_populates="students")
