-- Завдання 4
-- Створіть однотабличну базу даних «Овочі та фрукти»,
-- яка зберігатиме таку інформацію:
-- ■ Назва;
-- ■ Тип (овоч або фрукт);
-- ■ Колір;
-- ■ Калорійність;
-- ■ Короткий опис.

-- CREATE TABLE FRUITS_VEGETABLES (
--     ID SERIAL PRIMARY KEY,
--     NAME VARCHAR(50),
--     TYPE VARCHAR(10),
--     COLOR VARCHAR(30),
--     CALORIES INT,
--     DESCRIPTION TEXT
-- );

-- ЗАПОВНЕННЯ ДАНИМИ
-- INSERT INTO FRUITS_VEGETABLES (
--     NAME, TYPE, COLOR, CALORIES, DESCRIPTION
-- )
-- VALUES
-- ('APPLE', 'FRUIT', 'RED', 52, 'СОЛОДКИЙ ФРУКТ'),
-- ('BANANA', 'FRUIT', 'YELLOW', 89, 'ДУЖЕ ПОЖИВНИЙ ФРУКТ'),
-- ('CARROT', 'VEGETABLE', 'ORANGE', 41, 'КОРИСНИЙ ОВОЧ');

-- ЗАВДАННЯ 5

-- ■ Відображення всієї інформації з таблиці овочів та фруктів;
-- SELECT *
-- FROM FRUITS_VEGETABLES;

-- ВІДОБРАЖЕННЯ УСІХ ОВОЧІВ
-- SELECT *
-- FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'VEGETABLE';

-- ВІДОБРАЖЕННЯ УСІХ ФРУКТІВ
-- SELECT *
-- FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'FRUIT';

-- ВІДОБРАЖЕННЯ ВСІХ НАЗВ
-- SELECT NAME
-- FROM FRUITS_VEGETABLES;

-- ВІДОБРАЖЕННЯ УНІКАЛЬНИХ КОЛЬОРІВ
-- SELECT DISTINCT COLOR
-- FROM FRUITS_VEGETABLES;

-- ФРУКТИ ПЕВНОГО КОЛЬОРУ
-- SELECT *
-- FROM FRUITS_VEGETABLES
-- WHERE TYPE = 'FRUIT' AND COLOR = 'RED';

-- ОВОЧІ ПЕВНОГО КОЛЬОРУ
SELECT *
FROM FRUITS_VEGETABLES
WHERE TYPE = 'VEGETABLE' AND COLOR = 'ORANGE';
