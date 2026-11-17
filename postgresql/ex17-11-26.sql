--LeetCode: Replace Employee ID with the unique identifier
--Dificuldade: Fácil
--Objetivo: Encontrar todos os funcionários que possuem uma unique_id
SELECT EmployeeUNI.unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id