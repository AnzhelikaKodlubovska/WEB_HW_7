from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
from datetime import datetime
import random

fake = Faker()

engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()

groups = session.query(Group).all()
teachers = session.query(Teacher).all()
subjects = session.query(Subject).all()

for _ in range(30):
    student = Student(name=fake.name(), group=random.choice(groups))
    session.add(student)
    for subject in subjects:
        grade = Grade(student=student, subject=subject, score=random.randint(60, 100), date_received=fake.date_time_between(start_date='-1y', end_date='now'))
        session.add(grade)

session.commit()
