-- CREATE TABLE STUDENT_GRADES (
--     ID SERIAL,
--     FULL_NAME VARCHAR(100),
--     CITY VARCHAR(50),
--     COUNTRY VARCHAR(50),
--     BIRTH_DATE DATE,
--     EMAIL VARCHAR(100),
--     PHONE VARCHAR(20),
--     GROUP_NAME VARCHAR(50),
--     AVERAGE_GRADE FLOAT,
--     MIN_SUBJECT VARCHAR(50),
--     MAX_SUBJECT VARCHAR(50)
-- );

-- INSERT INTO STUDENT_GRADES (
--     FULL_NAME, CITY, COUNTRY, BIRTH_DATE, EMAIL, PHONE,
--     GROUP_NAME, AVERAGE_GRADE, MIN_SUBJECT, MAX_SUBJECT
-- )
-- VALUES
-- (
--     'Іван Петренко', 'Київ', 'Україна', '2000-05-12',
--     'ivan@gmail.com', '123456789',
--     'CS-101', 85.5, 'Математика', 'Інформатика'
-- ),
-- (
--     'Марія Іванова', 'Львів', 'Україна', '1999-11-23',
--     'maria@gmail.com', '987654321',
--     'CS-102', 90.2, 'Фізика', 'Програмування'
-- ),
-- (
--     'Олег Сидоренко', 'Одеса', 'Україна', '2001-03-08',
--     'oleg@gmail.com', '555666777',
--     'CS-103', 78.0, 'Хімія', 'Математика'
-- );

-- ВІДОБРАЗИТИ УСЮ ІНФОРМАЦІЮ
-- SELECT *
-- FROM STUDENT_GRADES;

-- ПОКАЗАТИ ПІБ УСІХ СТУДЕНТІВ
-- SELECT FULL_NAME
-- FROM STUDENT_GRADES;

-- ПОКАЗАТИ ВСІ СЕРЕДНІ ОЦІНКИ
-- SELECT AVERAGE_GRADE
-- FROM STUDENT_GRADES;

-- ПОКАЗАТИ ПІБ СТУДЕНТІВ З ОЦІНКОЮ БІЛЬШОЮ ЗА ЗАДАНУ
-- SELECT FULL_NAME
-- FROM STUDENT_GRADES
-- WHERE AVERAGE_GRADE > 80;

-- ПОКАЗАТИ КРАЇНИ(УНІКАЛЬНІ)
-- SELECT DISTINCT COUNTRY
-- FROM STUDENT_GRADES;

-- ПОКАЗАТИ МІСТА(УНІКАЛЬНІ)
-- SELECT DISTINCT CITY
-- FROM STUDENT_GRADES;

-- ПОКАЗАТИ НАЗВИ ГРУП(УНІКАЛЬНІ)
-- SELECT DISTINCT GROUP_NAME
-- FROM STUDENT_GRADES;

-- ПОКАЗАТИ НАЗВИ ПРЕДМЕТІВ З МІНІМАЛЬНИМИ ОЦІНКАМИ (УНІКАЛЬНІ)
-- SELECT DISTINCT MIN_SUBJECT, AVERAGE_GRADE
-- FROM STUDENT_GRADES;


-- SELECT *
-- FROM STUDENT_GRADES
-- WHERE CITY = 'Львів' OR CITY = 'Київ';

-- SELECT *
-- FROM STUDENT_GRADES
-- WHERE AVERAGE_GRADE BETWEEN 70 AND 80

-- ВИВЕСТИ ІМЯ, МІНІМАЛЬНУ ТА МАКСІМАЛЬНУ ОЦІНКУ ТА РІЗНИЦЮ МІЖ НИМИ
-- SELECT
--     FULL_NAME,
--     MIN(AVERAGE_GRADE) AS MIN_GRADE,
--     MAX(AVERAGE_GRADE) AS MAX_GRADE,
--     MAX(AVERAGE_GRADE) - MIN(AVERAGE_GRADE) AS DIFFERENCE
-- FROM STUDENT_GRADES
-- GROUP BY FULL_NAME;

-- ВИВЕСТИ МІСТА ТА МІСТА У НИЖНЬОМУ РЕГІСТРІ
-- SELECT
--     CITY,
--     LOWER(CITY) AS CITY_LOWER
-- FROM STUDENT_GRADES;

-- ВИВЕСТИ СТУДЕНТІВ ЧИЄ ПРІЗВИЩЕ ДОВШЕ НІЖ 13 СИМВОЛІВ
-- SELECT FULL_NAME
-- FROM STUDENT_GRADES
-- WHERE LENGTH(FULL_NAME) > 13;
