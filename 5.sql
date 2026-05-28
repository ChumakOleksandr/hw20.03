-- CREATE TABLE DEPARTMENTS (
--     ID SERIAL NOT NULL PRIMARY KEY ,
--     BUILDING INT NOT NULL CHECK (BUILDING BETWEEN 1 AND 5),
--     FINANCING INT NOT NULL  CHECK (FINANCING >= 0) DEFAULT 0,
--     NAME VARCHAR(100) NOT NULL UNIQUE CHECK (NAME <> '')
-- );

-- INSERT INTO DEPARTMENTS (BUILDING, FINANCING, NAME)
-- VALUES
-- (1, 50000, 'КАРДІОЛОГІЯ'),
-- (2, 30000, 'НЕВРОЛОГІЯ'),
-- (3, 45000, 'ХІРУРГІЯ'),
-- (4, 20000, 'ТЕРАПІЯ'),
-- (5, 35000, 'ПЕДІАТРІЯ'),

-- (1, 25000, 'ОНКОЛОГІЯ'),
-- (2, 15000, 'ДЕРМАТОЛОГІЯ'),
-- (3, 40000, 'ТРАНСПЛАНТОЛОГІЯ'),
-- (4, 18000, 'ІНФЕКЦІЙНЕ'),
-- (5, 29000, 'РЕАБІЛІТАЦІЯ'),

-- (1, 32000, 'ОФТАЛЬМОЛОГІЯ'),
-- (2, 22000, 'ОТОЛАРИНГОЛОГІЯ'),
-- (3, 28000, 'ЕНДОКРИНОЛОГІЯ'),
-- (4, 26000, 'УРОЛОГІЯ'),
-- (5, 15000, 'АЛЕРГОЛОГІЯ'),

-- (1, 41000, 'ІМУНОЛОГІЯ'),
-- (2, 17000, 'ПСИХІАТРІЯ'),
-- (3, 36000, 'ГЕМАТОЛОГІЯ'),
-- (4, 19000, 'НЕОНАТОЛОГІЯ'),
-- (5, 27000, 'ПУЛЬМОНОЛОГІЯ');

-- CREATE TABLE DISEASES (
--     ID SERIAL NOT NULL PRIMARY KEY,
--     NAME VARCHAR(100) NOT NULL UNIQUE CHECK (NAME <> ''),
--     SEVERITY INT NOT NULL DEFAULT 1 CHECK (SEVERITY >= 1)
-- );

-- INSERT INTO DISEASES (NAME, SEVERITY)
-- VALUES
-- ('ГРИП', 2),
-- ('ІНСУЛЬТ', 5),
-- ('ПНЕВМОНІЯ', 3),
-- ('ДІАБЕТ', 4),
-- ('АНГІНА', 1),

-- ('ГІПЕРТОНІЯ', 3),
-- ('АРИТМІЯ', 2),
-- ('БРОНХІТ', 2),
-- ('ОСТЕОХОНДРОЗ', 2),
-- ('СКОЛІОЗ', 2),

-- ('ГАСТРИТ', 2),
-- ('ВИРАЗКА', 4),
-- ('ГЕПАТИТ', 5),
-- ('НЕФРИТ', 3),
-- ('ЦИСТИТ', 1),

-- ('КАРІЄС', 1),
-- ('ОТИТ', 2),
-- ('СИНУСИТ', 2),
-- ('АЛЕРГІЯ', 1),
-- ('ПЕРЕЛОМ', 4);

-- CREATE TABLE DOCTORS (
--     ID SERIAL NOT NULL PRIMARY KEY,
--     NAME VARCHAR(255) NOT NULL CHECK (NAME <> ''),
--     SURNAME VARCHAR(255) NOT NULL CHECK (SURNAME <> ''),
--     PHONE CHAR(10),
--     SALARY INT NOT NULL CHECK (SALARY > 0)
-- );

-- INSERT INTO DOCTORS (NAME, SURNAME, PHONE, SALARY)
-- VALUES
-- ('ІВАН', 'ПЕТРЕНКО', '1000000001', 20000),
-- ('МАРІЯ', 'ІВАНОВА', '1000000002', 25000),
-- ('ОЛЕГ', 'СИДОРЕНКО', '1000000003', 22000),
-- ('БОРИС', 'КОВАЛЬ', '1000000004', 27000),
-- ('АННА', 'МЕЛЬНИК', '1000000005', 21000),

-- ('СЕРГІЙ', 'ТКАЧЕНКО', '1000000006', 24000),
-- ('НАТАЛІЯ', 'ШЕВЧЕНКО', '1000000007', 23000),
-- ('ЮРІЙ', 'БОНДАР', '1000000008', 26000),
-- ('ОЛЕНА', 'ЛИСЕНКО', '1000000009', 22500),
-- ('МИХАЙЛО', 'КРАВЕЦЬ', '1000000010', 25500),

-- ('ВІКТОР', 'ПАНЧЕНКО', '1000000011', 24500),
-- ('ІРИНА', 'МАРЧЕНКО', '1000000012', 23500),
-- ('ДЕНИС', 'РИБАК', '1000000013', 21500),
-- ('АЛІНА', 'ГОРОБЕЦЬ', '1000000014', 26500),
-- ('РОМАН', 'КУЗЬМЕНКО', '1000000015', 27500),

-- ('ТЕТЯНА', 'САВЧЕНКО', '1000000016', 24000),
-- ('ПАВЛО', 'МАЗУР', '1000000017', 23000),
-- ('ІГОР', 'ЧЕРНЕНКО', '1000000018', 25500),
-- ('ЄВГЕН', 'ДРОЗД', '1000000019', 26000),
-- ('НІНА', 'КОЗАК', '1000000020', 22000);

-- CREATE TABLE EXAMINATIONS (
--     ID SERIAL NOT NULL PRIMARY KEY,
--     NAME VARCHAR(100) NOT NULL UNIQUE CHECK (NAME <> ''),
--     DAYOFWEEK INT NOT NULL CHECK (DAYOFWEEK BETWEEN 1 AND 7),
--     STARTTIME TIME NOT NULL CHECK (STARTTIME BETWEEN '08:00' AND '18:00'),
--     ENDTIME TIME NOT NULL CHECK (ENDTIME > STARTTIME)
-- );

-- INSERT INTO EXAMINATIONS (NAME, DAYOFWEEK, STARTTIME, ENDTIME)
-- VALUES
-- ('УЗД', 1, '09:00', '10:00'),
-- ('РЕНТГЕН', 2, '10:00', '11:30'),
-- ('КТ', 3, '12:00', '13:00'),
-- ('МРТ', 4, '14:00', '15:30'),
-- ('АНАЛІЗ КРОВІ', 5, '08:30', '09:30'),

-- ('ЕКГ', 1, '10:30', '11:00'),
-- ('ФЛЮОРОГРАФІЯ', 2, '11:00', '12:00'),
-- ('БІОХІМІЯ КРОВІ', 3, '13:30', '14:30'),
-- ('КОЛОНОСКОПІЯ', 4, '15:30', '16:30'),
-- ('ГАСТРОСКОПІЯ', 5, '09:30', '10:30'),

-- ('ДОПЛЕР', 6, '10:00', '11:00'),
-- ('СПІРОМЕТРІЯ', 7, '11:30', '12:30'),
-- ('АЛЕРГІЧНІ ПРОБИ', 1, '12:30', '13:30'),
-- ('ГОРМОНАЛЬНИЙ АНАЛІЗ', 2, '14:00', '15:00'),
-- ('АНАЛІЗ СЕЧІ', 3, '08:00', '09:00'),

-- ('ІМУНОГРАМА', 4, '16:00', '17:00'),
-- ('ЕЛЕКТРОЕНЦЕФАЛОГРАФІЯ', 5, '13:00', '14:00'),
-- ('РЕОЕНЦЕФАЛОГРАФІЯ', 6, '09:00', '10:00'),
-- ('КАРДІОГРАФІЯ', 7, '10:00', '11:00'),
-- ('УЛЬТРАЗВУК СЕРЦЯ', 2, '15:00', '16:00');

-- CREATE TABLE WARDS (
--     ID SERIAL NOT NULL PRIMARY KEY,
--     BUILDING INT NOT NULL CHECK (BUILDING BETWEEN 1 AND 5),
--     FLOOR INT NOT NULL CHECK (FLOOR >= 1),
--     NAME VARCHAR(20) NOT NULL UNIQUE CHECK (NAME <> '')
-- );

-- INSERT INTO WARDS (BUILDING, FLOOR, NAME)
-- VALUES
-- (1, 1, 'ПАЛАТА-101'),
-- (2, 2, 'ПАЛАТА-202'),
-- (3, 3, 'ПАЛАТА-303'),
-- (4, 1, 'ПАЛАТА-104'),
-- (5, 2, 'ПАЛАТА-205'),

-- (1, 2, 'ПАЛАТА-102'),
-- (2, 3, 'ПАЛАТА-203'),
-- (3, 1, 'ПАЛАТА-304'),
-- (4, 2, 'ПАЛАТА-105'),
-- (5, 3, 'ПАЛАТА-206'),

-- (1, 3, 'ПАЛАТА-103'),
-- (2, 1, 'ПАЛАТА-201'),
-- (3, 2, 'ПАЛАТА-302'),
-- (4, 3, 'ПАЛАТА-106'),
-- (5, 1, 'ПАЛАТА-207'),

-- (1, 1, 'ПАЛАТА-108'),
-- (2, 2, 'ПАЛАТА-209'),
-- (3, 3, 'ПАЛАТА-310'),
-- (4, 1, 'ПАЛАТА-111'),
-- (5, 2, 'ПАЛАТА-212');

-- 1. Вивести вміст таблиці палат.
-- SELECT *
-- FROM WARDS;

-- 2. Вивести прізвища та телефони усіх лікарів.
-- SELECT SURNAME, PHONE
-- FROM DOCTORS;

-- 3. Вивести усі поверхи без повторень, де розміщуються палати.
-- SELECT DISTINCT FLOOR
-- FROM WARDS;

-- 4. Вивести назви захворювань під назвою « Name of
-- Disease» та ступінь їхньої тяжкості під назвою «Severity
-- of Disease».
-- SELECT
--     NAME AS "Name of Disease",
--     SEVERITY AS "Severity of Disease"
-- FROM DISEASES;

-- 5. Вивести назви відділень, які знаходяться у корпусі 5
-- з фондом фінансування меншим, ніж 30000.
-- SELECT NAME
-- FROM DEPARTMENTS
-- WHERE BUILDING = 5
-- AND FINANCING < 30000;

-- 6. Вивести назви відділень, які знаходяться у корпусі 3 з
-- фондом фінансування у діапазоні від 12000 до 15000.
-- SELECT NAME
-- FROM DEPARTMENTS
-- WHERE BUILDING = 3
-- AND FINANCING BETWEEN 12000 AND 15000;

-- 7. Вивести назви палат, які знаходяться у корпусах 4 та
-- 5 на 1-му поверсі.
-- SELECT NAME
-- FROM WARDS
-- WHERE BUILDING IN (4, 5)
-- AND FLOOR = 1;

-- 8. Вивести назви, корпуси та фонди фінансування відділень, які знаходяться у корпусах 3 або 6 та мають
-- фонд фінансування менший, ніж 11000 або більший
-- за 25000.
-- SELECT NAME, BUILDING, FINANCING
-- FROM DEPARTMENTS
-- WHERE BUILDING IN (3, 6)
-- AND (FINANCING < 11000 OR FINANCING > 25000);

-- 9. Вивести прізвища лікарів, зарплата (сума ставки та
-- надбавки 120) яких перевищує 1500.
-- SELECT SURNAME
-- FROM DOCTORS
-- WHERE (SALARY + 120) > 1500;

-- 10. Вивести прізвища лікарів, у яких половина зарплати
-- перевищує триразову надбавку у вигляді 500.
-- SELECT SURNAME
-- FROM DOCTORS
-- WHERE (SALARY / 2) > (500 * 3);

-- 11. Вивести назви обстежень без повторень, які проводяться у перші три дні тижня з 12:00 до 15:00.
-- SELECT DISTINCT NAME
-- FROM EXAMINATIONS
-- WHERE DAYOFWEEK BETWEEN 1 AND 3
-- AND STARTTIME >= '12:00'
-- AND ENDTIME <= '15:00';

-- 12.Вивести назви та номери корпусів відділень, які знаходяться у корпусах 1, 3, 8 або 10.
-- SELECT NAME, BUILDING
-- FROM DEPARTMENTS
-- WHERE BUILDING IN (1, 3, 8, 10);

-- 13. Вивести назви захворювань усіх ступенів тяжкості,
-- крім 1-го та 2-го.
-- SELECT NAME
-- FROM DISEASES
-- WHERE SEVERITY NOT IN (1, 2);

-- 14. Вивести назви відділень, які не знаходяться у
-- першому або третьому корпусі.
-- SELECT NAME
-- FROM DEPARTMENTS
-- WHERE BUILDING NOT IN (1, 3);

-- 15. Вивести назви відділень, які знаходяться у першому
-- або третьому корпусі.
-- SELECT NAME
-- FROM DEPARTMENTS
-- WHERE BUILDING IN (1, 3);

-- 16. Вивести прізвища лікарів, що починаються з літери
-- «К».
-- SELECT SURNAME
-- FROM DOCTORS
-- WHERE SURNAME ILIKE 'К%';

-- 17. Вивести кількість палат у кожному корпусі.
-- SELECT BUILDING, COUNT(*) AS WARD_COUNT
-- FROM WARDS
-- GROUP BY BUILDING;

-- 18. Вивести кількість палат на кожному поверсі.
-- SELECT FLOOR, COUNT(*) AS WARD_COUNT
-- FROM WARDS
-- GROUP BY FLOOR;

-- 19. Вивести середній фонд фінансування для кожного корпусу.
-- SELECT BUILDING, AVG(FINANCING) AS AVG_FINANCING
-- FROM DEPARTMENTS
-- GROUP BY BUILDING;

-- 20. Вивести максимальний фонд фінансування серед відділень у кожному корпусі.
-- SELECT BUILDING, MAX(FINANCING) AS MAX_FINANCING
-- FROM DEPARTMENTS
-- GROUP BY BUILDING;

-- 21. Вивести мінімальний фонд фінансування серед відділень у кожному корпусі.
-- SELECT BUILDING, MIN(FINANCING) AS MIN_FINANCING
-- FROM DEPARTMENTS
-- GROUP BY BUILDING;

-- 22. Вивести загальну суму фінансування для кожного корпусу.
-- SELECT BUILDING, SUM(FINANCING) AS TOTAL_FINANCING
-- FROM DEPARTMENTS
-- GROUP BY BUILDING;

-- 23. Вивести кількість відділень у кожному корпусі.
-- SELECT BUILDING, COUNT(*) AS DEPT_COUNT
-- FROM DEPARTMENTS
-- GROUP BY BUILDING;

-- 24. Вивести кількість захворювань для кожного ступеня тяжкості.
-- SELECT SEVERITY, COUNT(*) AS DISEASE_COUNT
-- FROM DISEASES
-- GROUP BY SEVERITY;

-- 25. Вивести середню зарплату лікарів залежно від наявності телефону.
-- SELECT
--     (PHONE IS NOT NULL) AS HAS_PHONE,
--     AVG(SALARY) AS AVG_SALARY
-- FROM DOCTORS
-- GROUP BY HAS_PHONE;

-- 28. Вивести кількість обстежень для кожного дня тижня.
-- SELECT DAYOFWEEK, COUNT(*) AS EXAM_COUNT
-- FROM EXAMINATIONS
-- GROUP BY DAYOFWEEK;

-- 29. Вивести найраніший час початку обстежень для кожного дня тижня.
-- SELECT DAYOFWEEK, MIN(STARTTIME) AS EARLIEST
-- FROM EXAMINATIONS
-- GROUP BY DAYOFWEEK;

-- 30. Вивести найпізніший час завершення обстежень для кожного дня тижня.
-- SELECT DAYOFWEEK, MAX(ENDTIME) AS LATEST
-- FROM EXAMINATIONS
-- GROUP BY DAYOFWEEK;

-- 31. вивести лікаря з найвищою зп
-- SELECT *
-- FROM DOCTORS
-- ORDER BY SALARY DESC
-- LIMIT 1;

-- 32. з найменшою
-- SELECT *
-- FROM DOCTORS
-- ORDER BY SALARY
-- LIMIT 1;

-- 33. лікарів в яких зп вище середньої
-- SELECT *
-- FROM DOCTORS
-- WHERE SALARY > (
--     SELECT AVG(SALARY)
--     FROM DOCTORS
-- );

-- 34. обстеження яке найраніше проводиться
-- SELECT *
-- FROM EXAMINATIONS
-- ORDER BY STARTTIME
-- LIMIT 1;
