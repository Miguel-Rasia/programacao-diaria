--LeetCode: Confirmation Rate
--Dificuldade: Média
--Objetivo: Descobrir a média de aceitação dos usuários
WITH confirmation_rate AS (
    SELECT
        c.user_id,
            CASE 
                WHEN c.action = 'confirmed' THEN 1
                WHEN c.action = 'timeout' THEN 0
            END AS confirmation_rate
    FROM Confirmations c
)


SELECT
    s.user_id,
    ROUND(COALESCE(AVG(c.confirmation_rate), 0), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN confirmation_rate c ON c.user_id = s.user_id
GROUP BY s.user_id