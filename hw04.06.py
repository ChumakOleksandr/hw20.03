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

# вивести імена та прізвища викладачів, які читають
# лекції в конкретній групі

# def show_teachers_by_group(session, group_name):
#     query = """
#     SELECT DISTINCT
#         T.NAME,
#         T.SURNAME
#     FROM GROUPS G
#     JOIN GROUPSLECTURES GL ON G.ID = GL.GROUPID
#     JOIN LECTURES L ON GL.LECTUREID = L.ID
#     JOIN TEACHERS T ON L.TEACHERID = T.ID
#     WHERE G.NAME = :group_name
#     """
#
#     results = session.execute(text(query), {"group_name": group_name})
#
#     for row in results:
#         print(row)
#
#
# show_teachers_by_group(session, "КН-101")

# вивести назви кафедр і груп, які до них відносяться

# def show_departments_and_groups(session):
#     query = """
#     SELECT
#         D.NAME AS DEPARTMENT,
#         G.NAME AS GROUP_NAME
#     FROM GROUPS G
#     JOIN DEPARTMENTS D ON G.DEPARTMENTID = D.ID
#     ORDER BY D.NAME, G.NAME
#     """
#
#     results = session.execute(text(query))
#
#     for row in results:
#         print(row)
#
#
# show_departments_and_groups(session)

# вивести інформацію про всіх викладачів


def show_all_teachers(session):
    query = """
    SELECT
        T.NAME,
        T.SURNAME,
        T.SALARY
    FROM TEACHERS T
    ORDER BY T.SURNAME
    """

    results = session.execute(text(query))

    for row in results:
        print(row)


show_all_teachers(session)
