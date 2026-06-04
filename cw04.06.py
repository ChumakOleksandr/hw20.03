import os

import dotenv
from sqlalchemy import MetaData, create_engine, text
from sqlalchemy.orm import sessionmaker

dotenv.load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DB")


db_uri = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"

engine = create_engine(db_uri)

Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
metadata.reflect(bind=engine)

# tables = metadata.tables
# print(list(tables.keys()))
#
# query = """
# SELECT *
# FROM DEPARTMENTS
# """
#
# query = text(query)
# result = session.execute(query)
#
# for row in result:
#     print(row)


# Завдання 2

# Вивести прізвища лікарів та їх спеціалізації;

# def show_doctors_specializations(session):
#     query = """
#     SELECT D.SURNAME, S.NAME
#     FROM DOCTORSSPECIALIZATIONS DS
#     JOIN DOCTORS D ON DS.DOCTORID = D.ID
#     JOIN SPECIALIZATIONS S ON DS.SPECIALIZATIONID = S.ID
#     ORDER BY D.SURNAME
#     """
#     results = session.execute(text(query))
#
#     for row in results:
#         print(row)
#

# show_doctors_specializations(session)

# Вивести прізвища та зарплати (сума ставки та надбавки)
# лікарів, які не перебувають у відпустці;

# def show_doctors_not_on_vacation(session):
#     query = """
#     SELECT D.SURNAME, (D.SALARY + D.PREMIUM) AS TOTAL_SALARY
#     FROM DOCTORS D
#     WHERE NOT EXISTS (
#         SELECT 1 FROM VACATIONS V
#         WHERE V.DOCTORID = D.ID
#         AND CURRENT_DATE BETWEEN V.STARTDATE AND V.ENDDATE
#     )
#     """
#     results = session.execute(text(query))
#
#     for row in results:
#         print(row)
#
#
# show_doctors_not_on_vacation(session)

# Вивести назви палат, які знаходяться у певному відділенні;

# def show_wards_in_department(session, department_name):
#     query = """
#     SELECT W.NAME
#     FROM WARDS W
#     JOIN DEPARTMENTS D ON W.DEPARTMENTID = D.ID
#     WHERE D.NAME = :dept
#     """
#     results = session.execute(text(query), {"dept": department_name})
#
#     for row in results:
#         print(row)
#

# show_wards_in_department(session, "КАРДІОЛОГІЯ")

#  Вивести усі пожертвування за вказаний місяць у
# вигляді: відділення, спонсор, сума пожертвування, дата
# пожертвування;

# def show_donations_by_month(session, month, year):
#     query = """
#     SELECT D.NAME, S.NAME, DN.AMOUNT, DN.DATE
#     FROM DONATIONS DN
#     JOIN DEPARTMENTS D ON DN.DEPARTMENTID = D.ID
#     JOIN SPONSORS S ON DN.SPONSORID = S.ID
#     WHERE EXTRACT(MONTH FROM DN.DATE) = :month
#     AND EXTRACT(YEAR FROM DN.DATE) = :year
#     """
#     results = session.execute(text(query), {"month": month, "year": year})
#
#     for row in results:
#         print(row)
#

# show_donations_by_month(session, 1, 2025)

# Вивести назви відділень без повторень, які спонсоруються певною компанією.


def show_departments_by_sponsor(session, sponsor_name):
    query = """
    SELECT DISTINCT D.NAME
    FROM DEPARTMENTS D
    JOIN DONATIONS DN ON DN.DEPARTMENTID = D.ID
    JOIN SPONSORS S ON DN.SPONSORID = S.ID
    WHERE S.NAME = :sponsor
    """
    results = session.execute(text(query), {"sponsor": sponsor_name})

    for row in results:
        print(row)


show_departments_by_sponsor(session, "UNITY HEALTH GROUP")
