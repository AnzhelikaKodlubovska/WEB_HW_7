from sqlalchemy import func, desc
from models import *

def select_1(session):
    students = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return students

def select_2(session, subject_name):
    student = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subject.has(name=subject_name)) \
        .group_by(Student.id).order_by(desc('avg_grade')).first()
    return student

def select_3(session, subject_name):
    avg_scores = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Group).filter(Grade.subject.has(name=subject_name)) \
        .group_by(Group.name).all()
    return avg_scores

def select_4(session):
    avg_score = session.query(func.round(func.avg(Grade.grade), 2)).scalar()
    return avg_score

def select_5(session, teacher_name):
    courses = session.query(Subject.name).join(Teacher).filter(Teacher.name == teacher_name).all()
    return courses

def select_6(session, group_name):
    students = session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()
    return students

def select_7(session, group_name, subject_name):
    grades = session.query(Grade.grade).join(Student).join(Group).join(Subject) \
        .filter(Group.name == group_name, Subject.name == subject_name).all()
    return grades

def select_8(session, teacher_name):
    avg_score = session.query(func.round(func.avg(Grade.grade), 2)).join(Subject).join(Teacher) \
        .filter(Teacher.name == teacher_name).scalar()
    return avg_score

def select_9(session, student_name):
    courses = session.query(Subject.name).join(Grade).join(Student) \
        .filter(Student.fullname == student_name).distinct().all()
    return courses

def select_10(session, student_name, teacher_name):
    courses = session.query(Subject.name).join(Grade).join(Student).join(Teacher) \
        .filter(Student.fullname == student_name, Teacher.name == teacher_name).distinct().all()
    return courses