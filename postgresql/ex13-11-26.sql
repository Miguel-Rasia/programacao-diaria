--LeetCode: Recyclable and Low Fat Products
--Dificuldade: fácil
--Objetivo: encontrar os product_id que é tanto low fat quanto recyclable

-- Write your PostgreSQL query statement below
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y'