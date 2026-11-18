--LeetCode: Product Sales Analysis 1
--Dificuldade: Fácil
--Objetivo: Juntar a tabela de vendas com a de produtos para obter mais informações sobre cada item
SELECT p.product_name, s.year, s.price
FROM Sales s
LEFT JOIN Product p ON s.product_id = p.product_id