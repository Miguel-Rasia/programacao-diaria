--LeetCode: Not Boring Movies
--Dificuldade: Fácil
--Objetivo: Exibir todos os filmes de índice ímpar que a descrição não seja 'boring'
SELECT *
FROM Cinema c
WHERE c.id % 2 = 1 AND c.description != 'boring'
ORDER BY c.rating DESC