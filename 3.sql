-- CREATE TABLE STUDENTS (
--     ID SERIAL PRIMARY KEY,
--     FULL_NAME VARCHAR(100),
--     CITY VARCHAR(50),
--     COUNTRY VARCHAR(50),
--     BIRTH_DATE DATE,
--     EMAIL VARCHAR(100),
--     PHONE VARCHAR(20),
--     GROUP_NAME VARCHAR(50),

--     MATH_GRADE INT,
--     PHYSICS_GRADE INT,
--     PROGRAMMING_GRADE INT,
--     INFORMATICS_GRADE INT
-- );

-- INSERT INTO STUDENTS (
--     FULL_NAME, CITY, COUNTRY, BIRTH_DATE, EMAIL, PHONE, GROUP_NAME,
--     MATH_GRADE, PHYSICS_GRADE, PROGRAMMING_GRADE, INFORMATICS_GRADE
-- )
-- VALUES
-- ('ІВАН ПЕТРЕНКО', 'КИЇВ', 'УКРАЇНА', '2004-05-12', 'IVAN@MAIL.COM', '123777456', 'CS-101',
--  80, 70, 65, 70),

-- ('МАРІЯ ІВАНОВА', 'ЛЬВІВ', 'УКРАЇНА', '2003-11-23', 'MARIA@MAIL.COM', '999777111', 'CS-101',
--  95, 90, 59, 88),

-- ('ОЛЕГ СИДОРЕНКО', 'ОДЕСА', 'УКРАЇНА', '2002-03-08', 'OLEG@MAIL.COM', '111222333', 'CS-102',
--  60, 65, 71, 92),

-- ('БОРИС КОВАЛЬ', 'КИЇВ', 'УКРАЇНА', '2004-07-19', 'BORIS@MAIL.COM', '777999888', 'CS-103',
--  85, 74, 90, 21);

-- ЗАВДАННЯ 1

-- Показати ПІБ усіх студентів з мінімальною оцінкою у вказаному діапазоні.
-- SELECT *
-- FROM STUDENTS
-- WHERE
--     MATH_GRADE = (SELECT MIN(MATH_GRADE) FROM STUDENTS)
--     OR PHYSICS_GRADE = (SELECT MIN(PHYSICS_GRADE) FROM STUDENTS)
--     OR PROGRAMMING_GRADE = (SELECT MIN(PROGRAMMING_GRADE) FROM STUDENTS)
--     OR INFORMATICS_GRADE = (SELECT MIN(INFORMATICS_GRADE) FROM STUDENTS);

-- СТУДЕНТИ, ЯКИМ 20 РОКІВ
-- SELECT *
-- FROM STUDENTS
-- WHERE DATE_PART('YEAR', AGE(CURRENT_DATE, BIRTH_DATE)) = 20;

-- СТУДЕНТИ У ДІАПАЗОНІ ВІКУ (НАПР: 20–23)
-- SELECT *
-- FROM STUDENTS
-- WHERE DATE_PART('YEAR', AGE(CURRENT_DATE, BIRTH_DATE)) BETWEEN 20 AND 23;

-- СТУДЕНТИ З ІМЕНЕМ "БОРИС"
-- SELECT *
-- FROM STUDENTS
-- WHERE FULL_NAME ILIKE 'БОРИС%';

-- НОМЕР МІСТИТЬ РІВНО 3 СІМКИ
-- SELECT *
-- FROM STUDENTS
-- WHERE LENGTH(PHONE) - LENGTH(REPLACE(PHONE, '7', '')) = 3;

-- EMAIL ПОЧИНАЄТЬСЯ З ЛІТЕРИ (НАПР. M)
-- SELECT EMAIL
-- FROM STUDENTS
-- WHERE EMAIL ILIKE 'M%';

-- ЗАВДАННЯ 2

-- МІНІМАЛЬНА СЕРЕДНЯ
-- SELECT MIN(
--     (MATH_GRADE + PHYSICS_GRADE + PROGRAMMING_GRADE + INFORMATICS_GRADE) / 4.0
-- )
-- FROM STUDENTS;

-- МАКСИМАЛЬНА СЕРЕДНЯ
-- SELECT MAX(
--     (MATH_GRADE + PHYSICS_GRADE + PROGRAMMING_GRADE + INFORMATICS_GRADE) / 4.0
-- )
-- FROM STUDENTS;

-- СТАТИСТИКА МІСТ
-- SELECT CITY, COUNT(*) AS STUDENT_COUNT
-- FROM STUDENTS
-- GROUP BY CITY;

-- СТАТИСТИКА ПО КРАЇНАХ
-- SELECT COUNTRY, COUNT(*) AS STUDENT_COUNT
-- FROM STUDENTS
-- GROUP BY COUNTRY;

-- КІЛЬКІСТЬ СТУДЕНТІВ З МІНІМАЛЬНОЮ ОЦІНКОЮ З МАТЕМАТИКИ
-- SELECT COUNT(*)
-- FROM STUDENTS
-- WHERE MATH_GRADE = (SELECT MIN(MATH_GRADE) FROM STUDENTS);

-- КІЛЬКІСТЬ СТУДЕНТІВ З МАКСИМАЛЬНОЮ ОЦІНКОЮ З МАТЕМАТИКИ
-- SELECT COUNT(*)
-- FROM STUDENTS
-- WHERE MATH_GRADE = (SELECT MAX(MATH_GRADE) FROM STUDENTS);

-- КІЛЬКІСТЬ СТУДЕНТІВ У КОЖНІЙ ГРУПІ
-- SELECT GROUP_NAME, COUNT(*) AS STUDENT_COUNT
-- FROM STUDENTS
-- GROUP BY GROUP_NAME;

-- СЕРЕДНЯ ПО ГРУПІ
-- SELECT GROUP_NAME,
-- AVG((MATH_GRADE + PHYSICS_GRADE + PROGRAMMING_GRADE + INFORMATICS_GRADE) / 4.0)
-- FROM STUDENTS
-- GROUP BY GROUP_NAME;

-- ВИВЕСТИ СТУДЕНТІВ ЯКІ НАВЧАЮТЬСЯ В ГРУПІ З НАЙВИЩОЮ СЕРЕДНЬОЇ ОЦІНКОЮ
-- SELECT *
-- FROM STUDENTS
-- WHERE GROUP_NAME = (
--     SELECT GROUP_NAME
--     FROM STUDENTS
--     GROUP BY GROUP_NAME
--     ORDER BY AVG(
--         (MATH_GRADE + PHYSICS_GRADE + PROGRAMMING_GRADE + INFORMATICS_GRADE) / 4.0
--     ) DESC
--     LIMIT 1
-- );

-- СТУДЕНТІВ ЯКІ НАВЧАЮТЬСЯ В МІСТІ ДЕ КІЛЬКІСТЬ СТУДЕНТІВ НИЖЧЧА ЗА СЕРЕДНЮ ПО МІСТАХ
-- WITH CITY_STATS AS (
--     SELECT CITY, COUNT(*) AS CNT
--     FROM STUDENTS
--     GROUP BY CITY
-- )
-- SELECT *
-- FROM STUDENTS
-- WHERE CITY IN (
--     SELECT CITY
--     FROM CITY_STATS
--     WHERE CNT < (SELECT AVG(CNT) FROM CITY_STATS)
--);

-- ВИВЕСТИ ГРУПИ ТА ЇХНІ СЕРЕДНІ ОЦІНКИ
-- WITH STUDENT_AVG AS (
--     SELECT GROUP_NAME,
--            (MATH_GRADE + PHYSICS_GRADE + PROGRAMMING_GRADE + INFORMATICS_GRADE) / 4.0 AS AVG_GRADE
--     FROM STUDENTS
-- )
-- SELECT GROUP_NAME, AVG(AVG_GRADE) AS GROUP_AVG
-- FROM STUDENT_AVG
-- GROUP BY GROUP_NAME;
