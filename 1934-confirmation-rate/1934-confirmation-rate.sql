SELECT 
    u.user_id, 
    ROUND(
        NVL(SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) / NULLIF(COUNT(c.action), 0), 0), 
        2
    ) AS confirmation_rate
FROM Signups u
LEFT JOIN Confirmations c ON u.user_id = c.user_id
GROUP BY u.user_id;