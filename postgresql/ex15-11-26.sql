--LeetCode: Article Views
--Dificuldade: Fácil
--Objetivo: Encontrar autores que visualizaram seus próprios artigos
SELECT DISTINCT author_id AS id
FROM VIEWS
WHERE author_id = viewer_id
ORDER BY id