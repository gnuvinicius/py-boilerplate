from typing import List, Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Course(Base):
    __tablename__ = 'tb_course'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30), unique=True)
    description: Mapped[Optional[str]]

    students: Mapped[List['Student']] = relationship(
        back_populates='course', cascade='all, delete-orphan')


class Student(Base):
    __tablename__ = 'tb_student'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("tb_course.id"))
    course: Mapped['Course'] = relationship(back_populates="students")
