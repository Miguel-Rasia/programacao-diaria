--LeetCode: Big Countries
--Dificuldade: Fácil
--Objetivo: Encontrar países que tenham população maior que 25 milhões e área maior que três milhões
SELECT name, population, area
FROM World
WHERE population >= 25000000 OR area >= 3000000