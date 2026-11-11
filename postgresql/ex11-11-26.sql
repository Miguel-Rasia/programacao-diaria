--LeetCode Find Customer Referee
--Dificuldade: Fácil
--Objetivo: Encontrar pessoas que são referenciadas por quem tem o id diferente de 2 ou não possui referencia nula

-- Write your PostgreSQL query statement below
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL