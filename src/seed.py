import random
from faker import Faker
from datetime import datetime, timedelta

from src.database import SessionLocal
from src.models import Group, Student, Teacher, Subject, Grade

fake = Faker("uk_UA")


def seed():
    session = SessionLocal()

    session.query(Grade).delete()
    session.query(Student).delete()
    session.query(Subject).delete()
    session.query(Teacher).delete()
    session.query(Group).delete()
    session.commit()

    groups = [Group(name="AD-101"), Group(name="AD-102"), Group(name="AD-103")]
    session.add_all(groups)
    session.commit()

    teachers = [Teacher(fullname=fake.name()) for _ in range(random.randint(3, 5))]
    session.add_all(teachers)
    session.commit()

    subject_names = [
        "Математика",
        "Фізика",
        "Програмування",
        "Бази даних",
        "Англійська",
        "Алгоритми",
        "Мережі",
        "Історія"
    ]
    random.shuffle(subject_names)
    subject_names = subject_names[:random.randint(5, 8)]

    subjects = []
    for name in subject_names:
        subjects.append(
            Subject(name=name, teacher=random.choice(teachers))
        )

    session.add_all(subjects)
    session.commit()

    students = []
    for _ in range(random.randint(30, 50)):
        students.append(
            Student(fullname=fake.name(), group=random.choice(groups))
        )

    session.add_all(students)
    session.commit()

    for student in students:
        grades_count = random.randint(10, 20)

        for _ in range(grades_count):
            grade = Grade(
                grade=random.randint(60, 100),
                student=student,
                subject=random.choice(subjects),
                date_received=datetime.now() - timedelta(days=random.randint(1, 365))
            )
            session.add(grade)

    session.commit()
    session.close()

    print("Database seeded successfully!")


if __name__ == "__main__":
    seed()