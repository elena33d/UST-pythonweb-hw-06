from sqlalchemy.orm import Session
from sqlalchemy import func, desc, cast, Numeric

from src.models import Student, Group, Teacher, Subject, Grade


def select_1(session: Session):
    return (
        session.query(
            Student.fullname,
            func.round(cast(func.avg(Grade.grade), Numeric), 2).label("avg_grade")
        )
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )


def select_2(session: Session, subject_id: int):
    return (
        session.query(
            Student.fullname,
            func.round(cast(func.avg(Grade.grade), Numeric), 2).label("avg_grade")
        )
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )


def select_3(session: Session, subject_id: int):
    return (
        session.query(
            Group.name,
            func.round(cast(func.avg(Grade.grade), Numeric), 2).label("avg_grade")
        )
        .select_from(Group)
        .join(Student)
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .order_by(desc("avg_grade"))
        .all()
    )


def select_4(session: Session):
    return session.query(
        func.round(cast(func.avg(Grade.grade), Numeric), 2)
    ).scalar()


def select_5(session: Session, teacher_id: int):
    return (
        session.query(Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )


def select_6(session: Session, group_id: int):
    return (
        session.query(Student.fullname)
        .filter(Student.group_id == group_id)
        .all()
    )


def select_7(session: Session, group_id: int, subject_id: int):
    return (
        session.query(
            Student.fullname,
            Grade.grade,
            Grade.date_received
        )
        .select_from(Student)
        .join(Grade)
        .filter(Student.group_id == group_id)
        .filter(Grade.subject_id == subject_id)
        .order_by(desc(Grade.date_received))
        .all()
    )


def select_8(session: Session, teacher_id: int):
    return (
        session.query(
            func.round(cast(func.avg(Grade.grade), Numeric), 2)
        )
        .select_from(Grade)
        .join(Subject)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )


# 9. Знайти список курсів, які відвідує певний студент
def select_9(session: Session, student_id: int):
    return (
        session.query(Subject.name)
        .select_from(Subject)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .group_by(Subject.id)
        .all()
    )


def select_10(session: Session, student_id: int, teacher_id: int):
    return (
        session.query(Subject.name)
        .select_from(Subject)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .filter(Subject.teacher_id == teacher_id)
        .group_by(Subject.id)
        .all()
    )