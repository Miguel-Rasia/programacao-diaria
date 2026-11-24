--LeetCode: Rising Temperature
--Dificuldade: Fácil
--Objetivo: Relacionar a tabela Weather com ela mesma e descobrir quais dias teve uma temperatura maior que o dia anterior
SELECT w1.id
FROM Weather w2
CROSS JOIN Weather as w1
WHERE w1.recordDate - w2.recordDate = 1 AND w1.temperature > w2.temperature