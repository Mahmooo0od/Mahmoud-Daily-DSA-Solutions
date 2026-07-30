SELECT *
FROM (
    SELECT 
        e.employee_id,
        e.employee_name,
        LEVEL AS "level",
        (
            SELECT COUNT(*) - 1
            FROM Employees
            CONNECT BY PRIOR employee_id = manager_id
            START WITH employee_id = e.employee_id
        ) AS team_size,
        (
            SELECT SUM(salary)
            FROM Employees
            CONNECT BY PRIOR employee_id = manager_id
            START WITH employee_id = e.employee_id
        ) AS budget
    FROM Employees e
    CONNECT BY PRIOR employee_id = manager_id
    START WITH manager_id IS NULL
)
ORDER BY 
    "level" ASC,
    budget DESC,
    employee_name ASC;