-- ЗАВДАННЯ 1

-- ОВОЧІ З КАЛОРІЙНІСТЮ МЕНШЕ ВКАЗАНОЇ
-- SELECT *
-- FROM PRODUCTS
-- WHERE TYPE = 'VEGETABLE'
-- AND CALORIES < 50;

-- ФРУКТИ В ДІАПАЗОНІ КАЛОРІЙ
-- SELECT *
-- FROM PRODUCTS
-- WHERE TYPE = 'FRUIT'
-- AND CALORIES BETWEEN 50 AND 90;

-- ОВОЧІ, У НАЗВІ ЯКИХ Є СЛОВО (НАПР. "КАПУСТА")
-- SELECT *
-- FROM PRODUCTS
-- WHERE TYPE = 'VEGETABLE'
-- AND NAME ILIKE '%КАПУСТА%';

-- ОВОЧІ ТА ФРУКТИ, ДЕ В ОПИСІ Є СЛОВО
-- SELECT *
-- FROM PRODUCTS
-- WHERE DESCRIPTION ILIKE '%ГЕМОГЛОБІН%';

-- ОВОЧІ ТА ФРУКТИ ЧЕРВОНОГО АБО ЖОВТОГО КОЛЬОРУ
-- SELECT *
-- FROM PRODUCTS
-- WHERE COLOR IN ('RED', 'YELLOW');

-- ЗАВДАННЯ 2

-- КІЛЬКІСТЬ ОВОЧІВ
-- SELECT COUNT(*)
-- FROM PRODUCTS
-- WHERE TYPE = 'VEGETABLE';

-- КІЛЬКІСТЬ ФРУКТІВ
-- SELECT COUNT(*)
-- FROM PRODUCTS
-- WHERE TYPE = 'FRUIT';

-- КІЛЬКІСТЬ ЗАДАНОГО КОЛЬОРУ
-- SELECT COUNT(*)
-- FROM PRODUCTS
-- WHERE COLOR = 'RED';

-- КІЛЬКІСТЬ ПО КОЖНОМУ КОЛЬОРУ
-- SELECT COLOR, COUNT(*) AS COUNT
-- FROM PRODUCTS
-- GROUP BY COLOR;

-- КОЛІР З МІНІМАЛЬНОЮ КІЛЬКІСТЮ
-- SELECT COLOR
-- FROM PRODUCTS
-- GROUP BY COLOR
-- ORDER BY COUNT(*)
-- LIMIT 1;

-- КОЛІР З МАКСИМАЛЬНОЮ КІЛЬКІСТЮ
-- SELECT COLOR
-- FROM PRODUCTS
-- GROUP BY COLOR
-- ORDER BY COUNT(*) DESC
-- LIMIT 1;

-- МІНІМАЛЬНА КАЛОРІЙНІСТЬ
-- SELECT MIN(CALORIES)
-- FROM PRODUCTS;

-- МАКСИМАЛЬНА КАЛОРІЙНІСТЬ
-- SELECT MAX(CALORIES)
-- FROM PRODUCTS;

-- СЕРЕДНЯ КАЛОРІЙНІСТЬ
-- SELECT AVG(CALORIES)
-- FROM PRODUCTS;

-- ФРУКТ З МІНІМАЛЬНОЮ КАЛОРІЙНІСТЮ
-- SELECT *
-- FROM PRODUCTS
-- WHERE TYPE = 'FRUIT'
-- ORDER BY CALORIES
-- LIMIT 1;

-- ФРУКТ З МАКСИМАЛЬНОЮ КАЛОРІЙНІСТЮ
-- SELECT *
-- FROM PRODUCTS
-- WHERE TYPE = 'FRUIT'
-- ORDER BY CALORIES DESC
-- LIMIT 1;
